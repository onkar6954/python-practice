# Stack two arrays vertically and horizontally.

import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8]])

arr1 = np.array([[1,2,3,4],
                 [5,6,7,8]])

print(np.hstack((arr,arr1)))
print(np.vstack((arr,arr1)))