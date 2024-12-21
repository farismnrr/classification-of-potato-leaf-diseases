import numpy as np

class FlippingGeometry:
    def __init__(self, image):
        self.image = image
        self.rows, self.cols, self.channels = image.shape
        self.flipped_image = np.zeros_like(image)

    def process(self, flip_code):
        if flip_code == 1:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.flipped_image[i, self.cols - j - 1] = self.image[i, j]

        elif flip_code == 0:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.flipped_image[self.rows - i - 1, j] = self.image[i, j]

        elif flip_code == -1:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.flipped_image[self.rows - i - 1, self.cols - j - 1] = self.image[i, j]

        return self.flipped_image