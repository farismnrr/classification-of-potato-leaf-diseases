import numpy as np

class NormalizationHistogram:
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

        # Calculate initial histogram
        histogram = np.zeros(self.L)
        for i in range(self.L):
            ni = np.sum(self.image == i)
            histogram[i] = ni / self.n

        # Calculate CDF
        CDF = np.zeros(self.L)
        CDF[0] = histogram[0]
        for i in range(1, self.L):
            CDF[i] = CDF[i-1] + histogram[i]

        # Normalize CDF
        CDF_normalized = CDF / CDF.max()

        # Apply normalization
        normalized_img = np.zeros_like(self.image, dtype=np.uint8)
        for i in range(self.height):
            for j in range(self.width):
                normalized_img[i, j] = np.uint8((self.L - 1) * CDF_normalized[self.image[i, j]])

        return normalized_img

    def get_histogram(self):
        histogram = np.zeros(self.L)
        for i in range(self.L):
            ni = np.sum(self.image == i)
            histogram[i] = ni / self.n
        return histogram