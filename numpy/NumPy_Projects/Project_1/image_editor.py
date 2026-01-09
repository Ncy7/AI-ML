import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

img = iio.imread("cow.jpg") # Reads the image file into a NumPy array. It has shape (height, width, 3) for RGB images.
print(img.shape) # Tells us the dimensions of the image array
print(img.dtype) # Tells us the data type of the image array

cropped_img = img[100:500, 200:600] # Crops the image to a specific region
iio.imwrite("cropped_img.jpg", cropped_img) # Saves the cropped image to a new file

img_int = img.astype(int) # Converts the image array to integer type
bright_img = img_int + 50 # Increases the brightness of the image
bright_img = np.clip(bright_img, 0, 255) # Ensures pixel values are within valid range
bright_img = bright_img.astype(np.uint8) # Converts back to unsigned 8-bit integer
iio.imwrite("bright_img.jpg", bright_img) # Saves the brightened image to a new file

contrast_img = img.copy()
contrast_img [contrast_img < 100] = 0
iio.imwrite("contrast_img.jpg", contrast_img) # Saves the high-contrast image to a new file

weights = np.array([0.2989, 0.5870, 0.1140]) # Weights for converting to grayscale
grayscale_img = img @ weights  # Converts the image to grayscale
grayscale_img = grayscale_img.astype(np.uint8) # Converts to unsigned 8-bit integer
iio.imwrite("grayscale_img.jpg", grayscale_img) # Saves the grayscale image to a new file

plt.imshow(grayscale_img, cmap='gray') # Displays the grayscale image
plt.show()