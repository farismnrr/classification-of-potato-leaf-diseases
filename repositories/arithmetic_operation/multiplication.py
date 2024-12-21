import numpy as np

class MultiplicationArithmetic:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2
        self.row = len(img1)
        self.col = len(img1[0])

    def process(self):
        result_image = np.zeros((self.row, self.col, 3), dtype=np.uint8)

        for i in range(self.row):
            for j in range(self.col):
                for k in range(3):
                    temp = int(self.img1[i, j, k]) * int(self.img2[i, j, k])
                    result_image[i, j, k] = min(255, max(0, temp))

        return result_image
