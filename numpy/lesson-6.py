# Aggregate function + summaroze data and typically returns a single value

import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])

""""
print(np.sum(array))          # Sum of all elements
print(np.mean(array))         # Mean of all elements
print(np.median(array))       # Median of all elements
print(np.std(array))          # Standard deviation of all elements
print(np.var(array))          # Variance of all elements
print(np.min(array))          # Minimum element
print(np.max(array))          # Maximum element
print(np.argmin(array))       # Index of minimum element
print(np.argmax(array))       # Index of maximum element
print(np.percentile(array, 25))  # 25th percentile
print(np.percentile(array, 50))  # 50th percentile (median)
print(np.percentile(array, 75))  # 75th percentile
print(np.cumsum(array))       # Cumulative sum of elements
print(np.cumprod(array))      # Cumulative product of elements
"""
print(np.sum(array, axis=0))    # Sum of each column
print(np.sum(array, axis=1))    # Sum of each row
