# -*- coding: utf8 -*-
#
'''
Better spy() function for Scipy sparse matrices.
'''
import matplotlib.pyplot as plt
import numpy


def plot(A, coloring):
    '''A better alternative for matplotlib's spy() function that uses the
    sparse data and maps it to a binary image.
    '''
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


def show(A, coloring='binary'):
    plot(A, coloring)
    plt.show()
    return


def save(A, filename, transparent=False, coloring='binary'):
    plot(A, coloring)
    plt.save(filename, transparent=transparent)
    return
