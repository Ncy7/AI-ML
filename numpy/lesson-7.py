# Filtering

import numpy as np
ages = np.array([[16, 25, 30],
                 [35, 40, 45],
                 [50, 55, 60]])

"""
# Create a boolean mask for ages greater than 40
mask = ages > 40
# Use the mask to filter the array
filtered_ages = ages[mask]
print("Ages greater than 40:", filtered_ages)
# Alternatively, filter directly without creating a separate mask
filtered_ages_direct = ages[ages > 40]
print("Ages greater than 40 (direct):", filtered_ages_direct)

adult_ages = ages[(ages > 40) & (ages < 60)]
print("Adult ages between 40 and 60:", adult_ages)

print("Original ages: ", ages)

# Output:
# Ages greater than 40: [45 50 55 60]
# Ages greater than 40 (direct): [45 50 55 60]
"""

adults = np.where(ages >= 18, ages, -1) # Replace ages < 18 with -1
print("Adults (ages >= 18):", adults)