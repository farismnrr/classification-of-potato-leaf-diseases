import numpy as np

class ScalarMultiplicationArithmetic:
    def __init__(self, img, brightness_factor):
        self.img = img
        self.brightness_factor = brightness_factor
        self.row = len(img)
        self.col = len(img[0])

    def process(self):
        result_image = np.zeros((self.row, self.col, 3), dtype=np.uint8)

        for i in range(self.row):
            for j in range(self.col):
                for k in range(3):
                    temp = int(self.img[i, j, k]) * self.brightness_factor
                    result_image[i, j, k] = min(255, max(0, temp))

        return result_image
