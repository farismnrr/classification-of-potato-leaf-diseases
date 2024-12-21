import numpy as np
import math

class RotationGeometry:
    def __init__(self, image):
        self.image = image
        self.rows, self.cols, self.channels = image.shape
        self.rotated_image = np.zeros_like(image)

    def process(self, angle):
        theta = math.radians(angle)
        center_x, center_y = self.rows // 2, self.cols // 2

        for i in range(self.rows):
            for j in range(self.cols):
                x_shifted = i - center_x
                y_shifted = j - center_y

                new_x = int(x_shifted * math.cos(theta) - y_shifted * math.sin(theta) + center_x)
                new_y = int(x_shifted * math.sin(theta) + y_shifted * math.cos(theta) + center_y)

                if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                    self.rotated_image[new_x, new_y] = self.image[i, j]

        return self.rotated_image