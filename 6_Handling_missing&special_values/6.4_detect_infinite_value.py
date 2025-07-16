"""
np.isinf() -> if 10/1000 or 1/0
              then we use np.isinf() for detecting infinite values

-> It returns a boolean value

Syntax -> np.isinf(array)

"""

import numpy as np

arr = np.array([1, 2, np.inf, -np.inf, 6])

print(np.isinf(arr))

# replace infinite value ->

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(cleaned_arr)