import numpy as np
import cv2

class LowpassFilter:
    def __init__(self, image):
        self.image = image
        self.kernel = np.ones((3, 3), np.float32) / 9
        
    def process(self):
        smoothed = cv2.filter2D(self.image, -1, self.kernel)
        return smoothed
