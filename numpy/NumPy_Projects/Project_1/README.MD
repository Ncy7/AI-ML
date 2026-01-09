Digital Image Processor

Objective: Manipulate an image using pure NumPy operations (slicing, broadcasting, masking) rather than using Photoshop

Concepts used in this project:

1. Image Data: An image is just a 3D grid of numbers representing Red, Green, and Blue intensity.

2. Slicing: You select a specific rectangular window of rows and columns to "crop" the grid.

3. Broadcasting: You apply a math operation to the entire array at once to update every pixel simultaneously (no loops).

4. Masking: You use a "True/False" question to find and modify only the specific pixels that match a condition.

5. Dot Product: You multiply the three color layers by specific weights and sum them up to "squash" the 3D array into a 2D grayscale image.
