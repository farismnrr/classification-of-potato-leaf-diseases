import numpy as np

class NegativeOperation:
    def __init__(self, img, threshold):
        self.img_array = img
        self.threshold = threshold
        self.height, self.width, self.channels = self.img_array.shape
        
    def process(self):
        negative_array = np.zeros_like(self.img_array)
        
        for i in range(self.height):
            for j in range(self.width):
                for c in range(self.channels):
                    negative_array[i, j, c] = np.int32(self.threshold) - np.int32(self.img_array[i, j, c])
        
        return negative_array