import numpy as np

class OtsuThresholding:
    def __init__(self, image):
        if len(image.shape) == 3:
            self.image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            self.image = image
        self.height, self.width = self.image.shape

    def process(self):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)

        # Calculate histogram
        histogram = np.zeros(256)
        for i in range(256):
            histogram[i] = np.sum(self.image == i)

        # Normalize histogram
        histogram = histogram / (self.height * self.width)

        # Calculate cumulative sums
        cumsum = np.cumsum(histogram)
        cumsum_vals = np.cumsum(np.arange(256) * histogram)

        # Initialize variables
        max_variance = 0
        threshold = 0
        total_mean = cumsum_vals[-1]

        # Find threshold that maximizes between-class variance
        for t in range(256):
            w0 = cumsum[t]
            w1 = 1 - w0

            if w0 == 0 or w1 == 0:
                continue

            mu0 = cumsum_vals[t] / w0
            mu1 = (total_mean - cumsum_vals[t]) / w1

            # Calculate between-class variance
            variance = w0 * w1 * (mu0 - mu1) ** 2

            # Update threshold if variance is larger
            if variance > max_variance:
                max_variance = variance
                threshold = t

        # Apply threshold
        binary = np.zeros_like(self.image)
        binary[self.image > threshold] = 255

        return binary
