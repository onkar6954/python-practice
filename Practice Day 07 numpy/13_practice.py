# Extract the last column from a 3×3 matrix.

import numpy as np

arr = np.array([[[1,2,3,4],
                 [5,6,7,8],
                 [9,0,1,2]],
                 [[3,4,5,6],
                  [7,8,9,0],
                  [1,2,3,4]]])

print(arr[1,[0,1,2],3])