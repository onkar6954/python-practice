# Find the minimum and maximum value in each row of a 2D array.

import numpy as np

arr = np.array([[2,3,4,5],
                [6,7,8,9],
                [7,5,3,5]])

print(np.min(arr,1))
print(np.max(arr,1))