import cv2
import numpy as np

class ErosionMorphology:
    def __init__(self, image):
        self.image = image

    def erode_manual(self, image, kernel):
        image_h, image_w = image.shape[:2]
        kernel_h, kernel_w = kernel.shape
        pad_h, pad_w = kernel_h // 2, kernel_w // 2

        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
        eroded_image = np.zeros_like(image)

        for i in range(image_h):
            for j in range(image_w):
                region = padded_image[i:i+kernel_h, j:j+kernel_w]
                eroded_image[i, j] = np.min(region * kernel)
        
        return eroded_image

    def process(self):
        if len(self.image.shape) == 3:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = self.image

        _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

        kernel_4x4 = np.ones((4, 4), dtype=np.uint8)
        kernel_6x6 = np.ones((6, 6), dtype=np.uint8)

        eroded_4x4 = self.erode_manual(binary_image, kernel_4x4)
        eroded_6x6 = self.erode_manual(binary_image, kernel_6x6)

        eroded_4x4_rgb = cv2.cvtColor(eroded_4x4, cv2.COLOR_GRAY2RGB)
        eroded_6x6_rgb = cv2.cvtColor(eroded_6x6, cv2.COLOR_GRAY2RGB)

        return eroded_4x4_rgb, eroded_6x6_rgb
