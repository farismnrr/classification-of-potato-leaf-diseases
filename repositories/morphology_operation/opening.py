import cv2
import numpy as np

class OpeningMorphology:
    def __init__(self, image):
        self.image = image

    def process(self):
        _, binary_image = cv2.threshold(self.image, 127, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))

        eroded_image = binary_image.copy()
        for _ in range(3):
            eroded_image = cv2.erode(eroded_image, kernel)

        dilated_image = eroded_image.copy()
        for _ in range(3):
            dilated_image = cv2.dilate(dilated_image, kernel)

        return eroded_image, dilated_image
