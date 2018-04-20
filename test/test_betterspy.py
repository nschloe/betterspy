# -*- coding: utf-8 -*-
#
import os
import tempfile

import imageio
import numpy
from scipy import sparse

import betterspy


def test_show():
    M = sparse.rand(20, 20, density=0.1)
    betterspy.show(M)
    return


def test_png():
    M = sparse.rand(20, 30, density=0.1, random_state=123)

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, 'test.png')
        betterspy.write_png(filepath, M, border_width=0)
        im = imageio.imread(filepath)
        numpy.random.seed(123)
        y = numpy.random.randint(0, 100, size=20*30)
        assert numpy.dot(y, im.flatten()) == 6967620

        filepath = os.path.join(temp_dir, 'border1.png')
        betterspy.write_png(filepath, M, border_width=1)
        im = imageio.imread(filepath)
        numpy.random.seed(123)
        y = numpy.random.randint(0, 100, size=22*32)
        assert numpy.dot(y, im.flatten()) == 7502920

        filepath = os.path.join(temp_dir, 'border_red.png')
        betterspy.write_png(filepath, M, border_width=1, border_color='red')
        im = imageio.imread(filepath)
        y = numpy.random.randint(0, 100, size=22*32*3)
        assert numpy.dot(y, im.flatten()) == 21627060

        filepath = os.path.join(temp_dir, 'viridis.png')
        betterspy.write_png(filepath, M, colormap='viridis')
        im = imageio.imread(filepath)
        y = numpy.random.randint(0, 100, size=20*30*3)
        assert numpy.dot(y, im.flatten()) == 5163692

        filepath = os.path.join(temp_dir, 'viridis-border1.png')
        betterspy.write_png(filepath, M, colormap='viridis', border_width=1)
        im = imageio.imread(filepath)
        y = numpy.random.randint(0, 100, size=22*32*3)
        assert numpy.dot(y, im.flatten()) == 6939887
    return


if __name__ == '__main__':
    test_png()
