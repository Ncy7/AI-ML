# Broadcasting allows NumPy to work with arrays
# with different shapes by virtually expanding dimensions
# # so they match jthe larger array's shape.

# The dimensions have the same size.
# or
# One of the dimensions is 1.

# shapes either match or one of them is 1.
# shapes meaning number of rows and columns.
# rows and columns either match or one of them is 1.

import numpy as np

array1 = np.array([[1,2,3,4,5,6,7,7,8,9,10]])      # shape (10,)
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])              # shape (10,1)

print(array1.shape)  # prints (1, 11)   
print(array2.shape)  # prints (10, 1)
print(array1 * array2)  # Broadcasting occurs here