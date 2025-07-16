"""
np.isnan() -> nan (not a number) when calculation is failed or data is missing in calculation
              eg. - 0/0,  |1 2|
                          |  4|
                           * missing value  
-> It returns a boolean value

Syntax - np.isnan(array)

"""

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(np.isnan(arr))

# true means, here value is missing 
# we can not compare directly -> print(np.nan == np.nan)