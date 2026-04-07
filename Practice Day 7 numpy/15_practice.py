# From a 5×5 matrix, extract the middle 3×3 submatrix.

import numpy as np

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,0],
                [1,2,3,4,5],
                [6,7,8,9,0],
                [1,2,3,4,5]])

arr2 = arr[1:4,1:4]
print(arr2)