import numpy as np

class EqualizationHistogram:
    def __init__(self, image, k=8, L=256):
        if len(image.shape) == 3:
            self.image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            self.image = image
        self.height, self.width = self.image.shape
        self.n = self.height * self.width
        self.k = k
        self.L = L

    def process(self):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)

        # Calculate histogram
        histogram = np.zeros(self.L)
        for i in range(self.L):
            histogram[i] = np.sum(self.image == i)

        # Normalize histogram
        histogram_normalized = histogram / self.n

        # Calculate CDF
        CDF = np.zeros(self.L)
        CDF[0] = histogram_normalized[0]
        for i in range(1, self.L):
            CDF[i] = CDF[i - 1] + histogram_normalized[i]

        # Calculate Ko (new intensity values)
        Ko = np.round(CDF * ((2 ** self.k) - 1))

        # Apply equalization
        equalized_img = np.zeros_like(self.image)
        for i in range(self.height):
            for j in range(self.width):
                equalized_img[i, j] = Ko[self.image[i, j]]

        return equalized_img.astype(np.uint8)

    def get_histogram(self):
        histogram = np.zeros(self.L)
        for i in range(self.L):
            ni = np.sum(self.image == i)
            histogram[i] = ni / self.n
        return histogram