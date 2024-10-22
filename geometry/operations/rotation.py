import numpy as np
import math

def rotate(image, angle):
    rows, cols, channels = image.shape
    rotated_image = np.zeros_like(image)

    theta = math.radians(angle)
    center_x, center_y = rows // 2, cols // 2

    for i in range(rows):
        for j in range(cols):
            x_shifted = i - center_x
            y_shifted = j - center_y

            new_x = int(x_shifted * math.cos(theta) - y_shifted * math.sin(theta) + center_x)
            new_y = int(x_shifted * math.sin(theta) + y_shifted * math.cos(theta) + center_y)

            if 0 <= new_x < rows and 0 <= new_y < cols:
                rotated_image[new_x, new_y] = image[i, j]

    return rotated_image