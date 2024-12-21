import cv2
import numpy as np

class ErosionEdgeMorphology:
    def __init__(self, image):
        self.image = image

    def erode_manual(self, image, kernel):
        image_h, image_w = image.shape
        kernel_h, kernel_w = kernel.shape
        pad_h, pad_w = kernel_h // 2, kernel_w // 2

        padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
        eroded_image = np.zeros_like(image)

        for i in range(image_h):
            for j in range(image_w):
                region = padded_image[i:i+kernel_h, j:j+kernel_w]
                eroded_image[i, j] = np.min(region * kernel)
        
        return eroded_image

    def process(self):
        _, binary_image = cv2.threshold(self.image, 127, 255, cv2.THRESH_BINARY)

        kernel = np.ones((3, 3), dtype=np.uint8)

        eroded_image = self.erode_manual(binary_image, kernel)
        edge_image = cv2.subtract(binary_image, eroded_image)

        return eroded_image, edge_image
