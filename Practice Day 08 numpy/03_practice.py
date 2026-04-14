# Replace all values < 50 with 0.

import numpy as np

arr = np.array([10, 60, 30, 80, 50, 45, 90])
arr [arr>50] = 0
print(arr)