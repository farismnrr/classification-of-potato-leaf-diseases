import numpy as np

class GrayscaleOperation:
    def __init__(self, img):
        self.r_weight = 0.299
        self.g_weight = 0.587 
        self.b_weight = 0.114
        self.img = img
        self.row = len(img)
        self.col = len(img[0])

    def process(self):
        b = self.img[:, :, 0]
        g = self.img[:, :, 1]
        r = self.img[:, :, 2]

        grayscale_array = np.zeros((self.row, self.col))

        for i in range(self.row):
            for j in range(self.col):
                grayscale_array[i, j] = (self.r_weight * r[i, j] + self.g_weight * g[i, j] + self.b_weight * b[i, j])

        grayscale_array = grayscale_array.astype(np.uint8)
        
        return grayscale_array