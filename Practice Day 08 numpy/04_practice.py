# Count how many elements are greater than the mean.

import numpy as np

arr = np.array([1, 3, 5, 8, 9, 12, 14, 15, 18, 20])

mean = arr.mean()

print(arr[arr>mean])