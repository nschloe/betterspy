# -*- coding: utf8 -*-
#
'''
Better spy() function for Scipy sparse matrices.
'''
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.ticker import MaxNLocator

import numpy
import png  # purepng


def plot(A, index0=0):
    m, n = A.shape
    plt.figure()
    plt.xlim(index0-0.5, index0+n-0.5)
    plt.ylim(index0-0.5, index0+m-0.5)

    ax = plt.gca()
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    # https://stackoverflow.com/a/34880501/353337
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    patches = [
        Rectangle((index0+col-0.5, index0+row-0.5), 1.0, 1.0)
        for row, cols in enumerate(A.tolil().rows)
        for col in cols
        ]
    p = PatchCollection(patches, color='k')
    ax.add_collection(p)
    return


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()
    return


def write_png(A, filename):
    m, n = A.shape

    w = png.Writer(n, m, greyscale=True, bitdepth=1)

    class RowIterator:
        def __init__(self, A):
            self.A = A.tocsr()
            self.current = 0
            return

        def __iter__(self):
            return self

        def __next__(self):
            if self.current >= A.shape[0]:
                raise StopIteration
            out = numpy.ones(A.shape[1], dtype=bool)
            out[self.A[self.current].indices] = False
            self.current += 1
            return out

    with open(filename, 'wb') as f:
        w.write(f, RowIterator(A))

    return
