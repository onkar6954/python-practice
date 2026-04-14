# Normalize an array (scale values between 0 and 1).

import numpy as np

arr = np.array([1, 3, 5, 8, 9, 12, 14, 15, 18, 20])

normilazed = (arr-np.min(arr))/(np.max(arr)-np.min(arr))

print(normilazed)