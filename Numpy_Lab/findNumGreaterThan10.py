
# Create a NumPy array from 1 to 15
# and find all numbers greater than 10.

import numpy as np

arr = np.arange(1,16)

result = arr[arr > 10]

print(result)

#output
#[11 12 13 14 15]