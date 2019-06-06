# -*- coding: utf-8 -*-
#
import os
import tempfile

import imageio
import numpy
import pytest
from scipy import sparse

import betterspy


def test_show():
    M = sparse.rand(20, 20, density=0.1)
    betterspy.show(M)
    return


@pytest.mark.parametrize(
    "ref, kwargs",
    [
        (6875310, {}),
        (7524085, {"border_width": 1}),
        (21306270, {"border_width": 1, "border_color": "red"}),
        (4981037, {"colormap": "viridis"}),
        (7101351, {"colormap": "viridis", "border_width": 1}),
    ],
)
def test_png(ref, kwargs):
    M = sparse.rand(20, 30, density=0.1, random_state=123)
    numpy.random.seed(123)

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, "test.png")
        betterspy.write_png(filepath, M, **kwargs)
        im = imageio.imread(filepath)
        y = numpy.random.randint(0, 100, size=numpy.prod(im.shape))
        assert numpy.dot(y, im.flatten()) == ref

    return


def test_readme_images():
    from dolfin import (
        MeshEditor,
        Mesh,
        FunctionSpace,
        assemble,
        EigenMatrix,
        dot,
        grad,
        dx,
        TrialFunction,
        TestFunction,
    )
    import meshzoo

    points, cells = meshzoo.rectangle(-1.0, 1.0, -1.0, 1.0, 20, 20)

    # Convert points, cells to dolfin mesh
    editor = MeshEditor()
    mesh = Mesh()
    # topological and geometrical dimension 2
    editor.open(mesh, "triangle", 2, 2, 1)
    editor.init_vertices(len(points))
    editor.init_cells(len(cells))
    for k, point in enumerate(points):
        editor.add_vertex(k, point[:2])
    for k, cell in enumerate(cells.astype(numpy.uintp)):
        editor.add_cell(k, cell)
    editor.close()

    V = FunctionSpace(mesh, "CG", 1)
    u = TrialFunction(V)
    v = TestFunction(V)
    L = EigenMatrix()
    assemble(dot(grad(u), grad(v)) * dx, tensor=L)
    A = L.sparray()

    # M = A.T.dot(A)
    M = A

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, "test.png")
        betterspy.write_png(filepath, M, border_width=2)

    # betterspy.write_png(
    #     'ATA.png', M, border_width=2,
    #     colormap='viridis'
    #     )
    return


if __name__ == "__main__":
    test_readme_images()
