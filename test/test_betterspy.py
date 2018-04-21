# -*- coding: utf-8 -*-
#
import os
import tempfile

import imageio
import numpy
from scipy import sparse

import betterspy
import pytest


def test_show():
    M = sparse.rand(20, 20, density=0.1)
    betterspy.show(M)
    return

@pytest.mark.parametrize(
    'ref, kwargs', [
    (6967620, {}),
    (7502920, {'border_width': 1}),
    (21370785, {'border_width': 1, 'border_color': 'red'}),
    (4986520, {'colormap': 'viridis'}),
    (6996597, {'colormap': 'viridis', 'border_width': 1}),
    ])
def test_png(ref, kwargs):
    M = sparse.rand(20, 30, density=0.1, random_state=123)
    numpy.random.seed(123)

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, 'test.png')
        betterspy.write_png(filepath, M, **kwargs)
        im = imageio.imread(filepath)
        y = numpy.random.randint(0, 100, size=numpy.prod(im.shape))
        assert numpy.dot(y, im.flatten()) == ref

    return


if __name__ == '__main__':
    test_png()
