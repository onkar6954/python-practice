# Convert an integer array into float type.

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.dtype)
arr2 = np.astype(arr,float)
print(arr2)
print(arr2.dtype)