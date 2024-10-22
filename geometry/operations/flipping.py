import numpy as np

def flip(image, flip_code):
    rows, cols, channels = image.shape
    flipped_image = np.zeros_like(image)

    if flip_code == 1:
        for i in range(rows):
            for j in range(cols):
                flipped_image[i, cols - j - 1] = image[i, j]

    elif flip_code == 0:
        for i in range(rows):
            for j in range(cols):
                flipped_image[rows - i - 1, j] = image[i, j]

    elif flip_code == -1:
        for i in range(rows):
            for j in range(cols):
                flipped_image[rows - i - 1, cols - j - 1] = image[i, j]

    return flipped_image