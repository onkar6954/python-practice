# Convert a 1D array of 12 elements into a 3×4 matrix.

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr2 = np.reshape(arr,(3,4))
print(arr2)