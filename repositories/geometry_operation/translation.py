import numpy as np

class TranslationGeometry:
    def __init__(self, image):
        self.image = image
        self.rows, self.cols, self.channels = image.shape
        self.translated_image = np.zeros_like(image)

    def process(self, shift_x, shift_y):
        for i in range(self.rows):
            for j in range(self.cols):
                new_x = i + shift_x
                new_y = j + shift_y
                if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                    self.translated_image[new_x, new_y] = self.image[i, j]

        return self.translated_image