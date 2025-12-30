# Random Numbers

import numpy as np
"""
rng = np.random.default_rng(seed=1)   # Create a random number generator

# print(rng.integers(low = 1, high = 7))          # Random integer between 1 and 6
print(rng.integers(low = 1, high = 101, size = 10))  # Array of 10 random integers between 1 and 100
print(rng.random(size = (3, 4)))                # 3x4 array of random floats between 0 and 1
print(rng.normal(loc = 0.0, scale = 1.0, size = (2, 3)))  # 2x3 array of random numbers from a normal distribution with mean 0 and stddev 1     
print(rng.choice(['red', 'blue', 'green'], size = 5))  # Array of 5 random choices from the given list
"""
"""
np.random.seed(seed=1)  # Set the seed for reproducibility
print(np.random.uniform(low=1, high=101, size=(3,2)))  # Array  of shape 3x2 with random floats between 1 and 100
"""
rng = np.random.default_rng()
"""
array  = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)  # Shuffle the array in place
print(array)
"""

# fruits = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
fruits = np.array(['🍎', '🍌', '🍒', '🍇', '🍓'])
fruit = rng.choice(fruits, size=(3,3))
print(fruit)

