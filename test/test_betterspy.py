# -*- coding: utf-8 -*-
#
from scipy import sparse

import betterspy


def test_show():
    A = sparse.rand(20, 20, density=0.1)
    M = sparse.csr_matrix(A)
    betterspy.show(M)
    return


def test_png():
    M = sparse.rand(20, 20, density=0.1).tocsr()
    betterspy.write_png(M, 'test.png')
    return


if __name__ == '__main__':
    test_png()
