import numpy as np

def translate(image, shift_x, shift_y):
    rows, cols, channels = image.shape
    translated_image = np.zeros_like(image)

    for i in range(rows):
        for j in range(cols):
            new_x = i + shift_x
            new_y = j + shift_y
            if 0 <= new_x < rows and 0 <= new_y < cols:
                translated_image[new_x, new_y] = image[i, j]

    return translated_image