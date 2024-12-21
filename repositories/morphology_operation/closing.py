import cv2
import numpy as np

class ClosingMorphology:
    def __init__(self, image):
        self.image = image
        
    def process(self):
        _, binary_image = cv2.threshold(self.image, 127, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (22, 22))

        closed_image = binary_image.copy()
        closed_image = cv2.dilate(closed_image, kernel)
        closed_image = cv2.erode(closed_image, kernel)

        return closed_image
