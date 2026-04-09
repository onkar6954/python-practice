# Find all elements divisible by 3.

import numpy as np

arr = np.array([1, 3, 5, 8, 9, 12, 14, 15, 18, 20])

arr1 = arr[arr%3==0]

print(arr)
print(arr1)