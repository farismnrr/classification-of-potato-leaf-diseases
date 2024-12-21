import numpy as np
import cv2

class HighpassFilter:
    def __init__(self, image):
        self.image = image
        self.kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        
    def process(self):
        highpass = cv2.filter2D(self.image, -1, self.kernel)
        return highpass
