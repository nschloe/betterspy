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


class RowIteratorBlackWhite:
    def __init__(self, A, border_width):
        self.A = A.tocsr()
        self.border_width = border_width
        # The border color must be 0.0 (black)
        self.current = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        m = self.A.shape[0]
        if self.current >= m + 2*self.border_width:
            raise StopIteration
        out = numpy.full(
            self.A.shape[1] + 2*self.border_width, True,
            dtype=numpy.bool
            )

        if self.current < self.border_width:
            out[:] = False
        elif self.current > m + self.border_width - 1:
            out[:] = False
        else:
            out[self.A[self.current-self.border_width].indices] = 0
            out[:self.border_width] = False
            if self.border_width > 0:
                out[-self.border_width:] = False

        self.current += 1
        return out


class RowIteratorGray:
    def __init__(self, A, border_width, border_color):
        self.A = A.tocsr()
        self.border_width = border_width
        self.border_color = border_color
        self.current = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        m = self.A.shape[0]
        if self.current >= m + 2*self.border_width:
            raise StopIteration
        out = numpy.full(
            self.A.shape[1] + 2*self.border_width, 255,
            dtype=numpy.int8
            )

        if self.current < self.border_width:
            out[:] = self.border_color
        elif self.current > m + self.border_width - 1:
            out[:] = self.border_color
        else:
            out[self.A[self.current-self.border_width].indices] = 0
            out[:self.border_width] = self.border_color
            if self.border_width > 0:
                out[-self.border_width:] = self.border_color

        self.current += 1
        return out


def write_png(A, filename, border_width=0, border_color=128):
    if border_width == 0:
        iterator = RowIteratorBlackWhite(A, border_width)
        bitdepth = 1
    else:
        iterator = RowIteratorGray(A, border_width, border_color)
        bitdepth = 8

    m, n = A.shape
    w = png.Writer(
        n+2*border_width, m+2*border_width, greyscale=True,
        bitdepth=bitdepth
        )

    with open(filename, 'wb') as f:
        w.write(f, iterator)

    return
