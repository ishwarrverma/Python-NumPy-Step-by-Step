"""
How to change data type's type?

.astype(new_type) -> age = '100' (str) 
                      age =  100  (int)

"""
import numpy as np
arr = np.array([1.2,2.5,3.8])
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)