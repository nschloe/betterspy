'''
Better spy() function for Scipy sparse matrices.
'''

from matplotlib import pyplot as pp
import numpy as np


def betterspy(A, coloring='binary'):
    '''A better alternative for matplotlib's spy() function that uses the
    sparse data and maps it to a binary image.
    '''

    m, n = A.shape

    if coloring == 'binary':
        X = np.zeros((m, n), dtype=bool)
        X[:] = False
        for i, row in enumerate(A.tolil().rows):
            X[i, row] = True

    elif coloring == 'checkboard':
        X = np.zeros((m, n), dtype=float)
        X[:] = 0.0
        for i, row in enumerate(A.tolil().rows):
            for j in row:
                X[i, j] = 1.0 if ((i+j) % 2) else 0.8

    elif coloring == 'value':
        X = np.zeros((m, n), dtype=float)
        X[:] = 0.0
        Alil = A.tolil()
        for i, row in enumerate(Alil.rows):
            for k, j in enumerate(row):
                X[i, j] = abs(Alil.data[i][k])

    else:
        raise ValueError('Illegal coloring \'%s\'.' % coloring)

    pp.imshow(X,
              cmap='Greys',
              interpolation='nearest',
              )
    return
