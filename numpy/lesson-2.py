# Mutidimensional arrays in Python using NumPy

import numpy as np
# For the numbers
array = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [0, 1, 2]]])  # creates a 3D numpy array
print(array.ndim)  # prints the number of dimensions
print(array.shape)  # prints the shape of the array. Output: (3, 2, 3) (depth, rows, columns)
print(array.size)  # prints the total number of elements
print(array[1, 0, 2])  # accesses the element at depth 1, row 0, column 2

word = array[1,0,2] + np.array([1,2,3]) # works like 3 + [1, 2, 3] or [3+1, 3+2, 3+3]
word1 = array[1,0,2] + array[1,1,2]
print(word1)  # prints the sum of two accessed elements
print(word)  # prints the accessed element plus the list [1,2,3]

# For the strings
str_array = np.array([[["Hello", "World"], ["Welcome", "To"]],
                      [["NumPy", "Tutorial"], ["For", "Beginners"]],
                      [["Have", "A"], ["Great", "Day"]]])  # creates a 3D numpy array of strings
print(str_array.ndim)  # prints the number of dimensions
print(str_array.shape)  # prints the shape of the array. Output: (3, 2, 2) (depth, rows, columns)
print(str_array.size)  # prints the total number of elements
print(str_array[2, 1, 0])  # accesses the element at depth 2, row 1, column 0
greeting = str_array[0, 0, 0] + " " + str_array[0, 0, 1]  # concatenates two accessed strings
print(greeting)  # prints "Hello World"

