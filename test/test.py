

import betterspy
from PIL import Image
import scipy.sparse as sps

A = sps.rand(200, 200, density=0.01)
M = sps.csr_matrix(A)

#plt.spy(M)
#betterspy.spy(A)


im = Image.new('1', M.shape, 1)
for i, row in enumerate(A.tolil().rows):
    for j in row:
        im.putpixel((i, j), 0)

im.save('test.png')
im.show()
