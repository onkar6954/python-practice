# Append an element to an existing array.

import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8]])

arr2 = np.append(arr,[9,0,1,2]).reshape((3,4))
print(arr2)