# -*- coding: utf-8 -*-
#
from scipy import sparse

import betterspy


def test_show():
    M = sparse.rand(20, 20, density=0.1)
    betterspy.show(M)
    return


def test_png():
    M = sparse.rand(20, 20, density=0.1)
    betterspy.write_png(M, 'test.png')
    return


if __name__ == '__main__':
    test_png()
