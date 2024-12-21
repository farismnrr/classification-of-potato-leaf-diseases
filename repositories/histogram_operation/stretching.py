import numpy as np

class StretchingHistogram:
    def __init__(self, image, L=256):
        if len(image.shape) == 3:
            self.image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            self.image = image
        self.height, self.width = self.image.shape
        self.n = self.height * self.width
        self.L = L

    def process(self):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)

        # Calculate gamma min and max
        gamma_min = np.min(self.image)
        gamma_max = np.max(self.image)

        # Apply stretching formula
        stretched_img = (self.image - gamma_min) / (gamma_max - gamma_min) * 255
        stretched_img = stretched_img.astype(np.uint8)

        return stretched_img

    def get_histogram(self):
        histogram = np.zeros(self.L)
        for i in range(self.L):
            ni = np.sum(self.image == i)
            histogram[i] = ni / self.n
        return histogram