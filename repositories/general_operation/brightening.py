import numpy as np

class BrighteningOperation:
    def __init__(self, img, brightness_factor):
        self.img = img
        self.brightness_factor = brightness_factor
        self.row = len(img)
        self.col = len(img[0])
        
    def process(self):
        b = self.img[:, :, 0]
        g = self.img[:, :, 1]
        r = self.img[:, :, 2]

        brightened_b = np.zeros((self.row, self.col), dtype=np.uint8)
        brightened_g = np.zeros((self.row, self.col), dtype=np.uint8)
        brightened_r = np.zeros((self.row, self.col), dtype=np.uint8)

        for i in range(self.row):
            for j in range(self.col):
                temp_b = int(b[i, j]) + self.brightness_factor
                temp_g = int(g[i, j]) + self.brightness_factor
                temp_r = int(r[i, j]) + self.brightness_factor
                
                brightened_b[i, j] = min(255, max(0, temp_b))
                brightened_g[i, j] = min(255, max(0, temp_g))
                brightened_r[i, j] = min(255, max(0, temp_r))

        return np.dstack((brightened_b, brightened_g, brightened_r))