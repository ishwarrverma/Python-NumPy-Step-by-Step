#Creating arrays from python lists

#np.array([elem1, elem2, elem3, elem4, elem,5])

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

# create with default value - use for future values and also known as a zeroes array
#np.zeros(shape) -> (4) for 1d, (4,4) for 2d

zeroes_array = np.zeros(3)
print(zeroes_array)

#ones(shape) - for defaulting 1 

ones_array = np.ones([2,3])
print(ones_array)

#full(shape,value) - for defaulting a specific value

filled_array = np.full((2,2),8)
print(filled_array)