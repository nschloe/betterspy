# -*- coding: utf-8 -*-
#
from scipy import sparse

import betterspy


def test():
    A = sparse.rand(20, 20, density=0.1)
    M = sparse.csr_matrix(A)
    betterspy.show(M)
    return


if __name__ == '__main__':
    test()
