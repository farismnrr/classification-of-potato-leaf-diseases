import numpy as np

class GlobalsThresholding:
    def __init__(self, image, threshold):
        if len(image.shape) == 3:
            self.image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            self.image = image
        self.threshold = threshold
        self.height, self.width = self.image.shape

    def process(self):
        self.image = self.image.astype(np.uint8)
        binary = np.zeros_like(self.image)
        binary[self.image > self.threshold] = 255
        
        return binary

    def basic(self):
        return self.process()
        
    def inverse(self):
        self.image = self.image.astype(np.uint8)
        binary = np.zeros_like(self.image)
        binary[self.image <= self.threshold] = 255

        return binary

    def truncate(self):
        self.image = self.image.astype(np.uint8)
        output = self.image.copy()
        output[output > self.threshold] = self.threshold

        return output

    def to_zero(self):
        self.image = self.image.astype(np.uint8)
        output = np.zeros_like(self.image)
        output[self.image > self.threshold] = self.image[self.image > self.threshold]

        return output

    def to_zero_inverse(self):
        self.image = self.image.astype(np.uint8)
        output = np.zeros_like(self.image)
        output[self.image <= self.threshold] = self.image[self.image <= self.threshold]

        return output
