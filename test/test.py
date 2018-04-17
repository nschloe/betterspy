# -*- coding: utf-8 -*-
#
from scipy import sparse

import betterspy


def test():
    A = sparse.rand(200, 200, density=0.01)
    M = sparse.csr_matrix(A)
    betterspy.show(M)
    return


if __name__ == '__main__':
    test()
