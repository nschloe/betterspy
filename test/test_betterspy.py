# -*- coding: utf-8 -*-
#
from scipy import sparse

import betterspy


def test_show():
    M = sparse.rand(20, 20, density=0.1)
    betterspy.show(M)
    return


def test_png():
    M = sparse.rand(20, 30, density=0.1)
    betterspy.write_png(M, 'test.png', border_width=0)
    betterspy.write_png(M, 'border1.png', border_width=1)
    betterspy.write_png(M, 'viridis.png', colormap='viridis')
    return


if __name__ == '__main__':
    test_png()
