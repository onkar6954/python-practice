# Find indices where elements are even.

import numpy as np

# arr = np.array([1, 3, 5, 8, 9, 12, 14, 15, 18, 20])
# print(np.argwhere(arr%2==0))

arr2d = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(np.argwhere(arr2d%2==0))
print(arr)