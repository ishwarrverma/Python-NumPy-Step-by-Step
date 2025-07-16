"""
np.insert() - with this we can insert an element in a perticular or specific position

syntax - np.insert(array, index, value, axis=None)

                     array -> original array
                     index -> index no. (position no.)
                     value -> data
                     axis -> None (flatten array)
                     axis=0 -> row wise
                     axis=1 -> column wise
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 100)
print(new_arr)