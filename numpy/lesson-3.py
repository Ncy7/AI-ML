# Slicing in numpy
import numpy as np

array  = np.array ([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]])

# array[start:stop:step , start:stop:step]
print(array[0])  # prints the first row
print(array[1])  # prints the second row
print(array[2])  # prints the third row
print(array[3])  # prints the fourth row

print(array[-1])  # prints the last row
print(array[-2])  # prints the second last row
print(array[-3])  # prints the third last row
print(array[-4])  # prints the fourth last row

print(array[0:3])   # prints rows from index 0 to 2
print(array[1:4])   # prints rows from index 1 to 3
print(array[::2])   # prints every second row   
print(array[0:4:2]) # prints rows from index 0 to 3 with a step of 2
print(array[::-1])  # prints all rows in reverse order
print(array[::])    # prints all rows
print(array[:])     # prints all rows
print(array[:2])    # prints rows from the start to index 1
print(array[2:])    # prints rows from index 2 to the end

print(array[:,0])   # prints the first column # [row, column] Here : means all rows and 0 means first column
print(array[:,1])   # prints the second column
print(array[:,2])   # prints the third column
print(array[:,3])   # prints the fourth column

print(array[:,:2])   # prints first two columns
print(array[:,1:3])  # prints columns from index 1 to 2 
print(array[:,::2])  # prints every second column
print(array[:,0:4:2])# prints columns from index 0 to 3 with a step of 2
print(array[:,::-1]) # prints all columns in reverse order  
print(array[:,::])   # prints all columns
print(array[:,:])    # prints all columns
print(array[0:2,2:4]) # prints a sub-array from rows 0 to 1 and columns 2 to 3
print(array[1:3,0:2]) # prints a sub-array from rows 1 to 2 and columns 0 to 1