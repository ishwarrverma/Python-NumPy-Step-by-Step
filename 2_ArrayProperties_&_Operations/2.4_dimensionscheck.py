"""
How to check dimensions of an Array?

.ndim -> get total number of dimensions (1d array, 2d array or 3d array)

"""

import numpy as np
arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],
                   [4,5,6]])
arr_3d = np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)