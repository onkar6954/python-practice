# Find .shape, .size, .ndim of a 3D array you create yourself.

import numpy as np

arr = np.array([[[1,2,3],
                 [1,2,3]],
                 [[1,2,3],
                  [1,2,3]]])

print(arr.shape)
print(arr.size)
print(arr.ndim)