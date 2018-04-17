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


def save(A, filename, transparent=False):
    plot(A)
    plt.save(filename, transparent=transparent)
    return


def save_png(A, coloring='binary'):
    m, n = A.shape

    if coloring == 'binary':
        X = numpy.zeros((m, n), dtype=bool)
        for i, row in enumerate(A.tolil().rows):
            X[i, row] = True

    elif coloring == 'checkboard':
        X = numpy.zeros((m, n), dtype=float)
        for i, row in enumerate(A.tolil().rows):
            for j in row:
                X[i, j] = 1.0 if ((i+j) % 2) else 0.8

    else:
        assert coloring == 'value', 'Illegal coloring \'{}\'.'.format(coloring)
        X = numpy.zeros((m, n), dtype=float)
        Alil = A.tolil()
        for i, row in enumerate(Alil.rows):
            for k, j in enumerate(row):
                X[i, j] = abs(Alil.data[i][k])

    plt.imshow(X, cmap='Greys', interpolation='nearest')
    return
