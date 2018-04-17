# -*- coding: utf8 -*-
#
'''
Better spy() function for Scipy sparse matrices.
'''
from matplotlib import pyplot as plt
import numpy

__version__ = '0.1.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/betterspy'


def spy(A, coloring='binary'):
    '''A better alternative for matplotlib's spy() function that uses the
    sparse data and maps it to a binary image.
    '''

    m, n = A.shape

    if coloring == 'binary':
        X = numpy.zeros((m, n), dtype=bool)
        X[:] = False
        for i, row in enumerate(A.tolil().rows):
            X[i, row] = True

    elif coloring == 'checkboard':
        X = numpy.zeros((m, n), dtype=float)
        for i, row in enumerate(A.tolil().rows):
            for j in row:
                X[i, j] = 1.0 if ((i+j) % 2) else 0.8

    elif coloring == 'value':
        X = numpy.zeros((m, n), dtype=float)
        Alil = A.tolil()
        for i, row in enumerate(Alil.rows):
            for k, j in enumerate(row):
                X[i, j] = abs(Alil.data[i][k])

    else:
        raise ValueError('Illegal coloring \'%s\'.' % coloring)

    plt.imshow(X, cmap='Greys', interpolation='nearest')

    return
