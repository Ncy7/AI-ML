# Arithmetic on Numpy

import numpy as np

"""

# Scalar arithmetic
array1 = np.array([10, 20, 30, 40, 50])
print(array1 + 5)    # adds 5 to each element
print(array1 - 2)    # subtracts 2 from each element
print(array1 * 3)    # multiplies each element by 3
print(array1 / 10)   # divides each element by 10
print(array1 ** 2)   # squares each element
print(array1 % 4)    # modulus of each element by 4
print(np.sqrt(array1))  # square root of each element
print(np.log(array1))   # natural logarithm of each element
print(np.exp(array1))   # exponential of each element
print(np.sin(array1))   # sine of each element (in radians)
print(np.cos(array1))   # cosine of each element (in radians)
print(np.round(array1 / 3))  # rounds the result of division to nearest integer

"""

"""
# Vectorized arithmetic

radii = np.array([1, 2, 3,])
print(2 * np.pi * radii)  # circumference of circles with given radii
areas = np.pi * radii**2
print(areas)              # area of circles with given radii
diameters = 2 * radii
print(diameters)          # diameter of circles with given radii

"""

"""
# Element-wise arithmetic between arrays
array1 = np.array([4,5,6])
array2 = np.array([1,2,3])
print(array1 + array2)  # adds corresponding elements
print(array1 - array2)  # subtracts corresponding elements
print(array1 * array2)  # multiplies corresponding elements
print(array1 / array2)  # divides corresponding elements
print(array1 ** array2) # raises elements of array1 to the power of corresponding elements in array2

"""

# Comparison operations between arrays
scores =  np.array([10, 20, 30, 40, 50])
print(scores > 25)   # checks which elements are greater than 25
print(scores < 25)   # checks which elements are less than 25   

scores[scores < 25] = 0  # sets elements less than 25 to 0
print(scores)

print(scores >= 30)  # checks which elements are greater than or equal to 30
print(scores <= 30)  # checks which elements are less than or equal to 30
print(scores == 40)  # checks which elements are equal to 40
print(scores != 40)  # checks which elements are not equal to 40
print((scores > 20) & (scores < 50))  # checks which elements are greater than 20 and less than 50
print((scores < 20) | (scores > 40))  # checks which elements are less than 20 or greater than 40
