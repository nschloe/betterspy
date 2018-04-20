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


class RowIterator:
    def __init__(self, A, border_width, border_color, colormap):
        self.A = A.tocsr()
        self.border_width = border_width

        if self.border_width == 0 and colormap is None:
            self.border_color = False
            self.bitdepth = 1
            self.dtype = numpy.bool

            def convert_values(idx, vals):
                out = numpy.ones(self.A.shape[1], dtype=self.dtype)
                out[idx] = False
                return out

            self.convert_values = convert_values

        elif colormap is None:
            self.border_color = border_color
            self.bitdepth = 8
            self.dtype = numpy.int8

            def convert_values(idx, vals):
                out = numpy.full(self.A.shape[1], 255, dtype=self.dtype)
                out[idx] = 0
                return out

            self.convert_values = convert_values

        else:
            assert False
            self.border_color = border_color
            self.zero_color = 255
            self.dtype = numpy.int8
            self.bitdepth = 8

        self.current = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        m = self.A.shape[0]
        b = self.border_width

        if self.current >= m + 2*b:
            raise StopIteration

        if b == 0:
            row = self.A[self.current-b]
            out = self.convert_values(row.indices, row.data)
        else:
            out = numpy.empty(self.A.shape[1] + 2*b, dtype=self.dtype)
            out[:b] = self.border_color
            out[-b:] = self.border_color
            if self.current < b:
                out[b:-b] = self.border_color
            elif self.current > m + b - 1:
                out[b:-b] = self.border_color
            else:
                row = self.A[self.current-b]
                out[b:-b] = self.convert_values(row.indices, row.data)

        self.current += 1
        return out


def write_png(A, filename, border_width=0, border_color=128, colormap=None):
    iterator = RowIterator(A, border_width, border_color, colormap)

    m, n = A.shape
    w = png.Writer(
        n+2*border_width, m+2*border_width, greyscale=True,
        bitdepth=iterator.bitdepth
        )

    with open(filename, 'wb') as f:
        w.write(f, iterator)

    return
