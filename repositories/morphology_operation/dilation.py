import cv2
import numpy as np

class DilationMorphology:
    def __init__(self, image):
        self.image = image

    def dilate_manual(self, image, kernel):
        image_h, image_w = image.shape[:2]
        kernel_h, kernel_w = kernel.shape
        pad_h, pad_w = kernel_h // 2, kernel_w // 2

        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
        dilated_image = np.zeros_like(image)

        for i in range(image_h):
            for j in range(image_w):
                region = padded_image[i:i+kernel_h, j:j+kernel_w]
                dilated_image[i, j] = np.max(region * kernel)
        
        return dilated_image

    def process(self):
        if len(self.image.shape) == 3:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = self.image

        _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

        kernel_4x4 = np.ones((4, 4), dtype=np.uint8)
        kernel_7x7 = np.ones((7, 7), dtype=np.uint8)

        dilated_4x4 = self.dilate_manual(binary_image, kernel_4x4)
        dilated_7x7 = self.dilate_manual(binary_image, kernel_7x7)

        dilated_4x4_rgb = cv2.cvtColor(dilated_4x4, cv2.COLOR_GRAY2RGB)
        dilated_7x7_rgb = cv2.cvtColor(dilated_7x7, cv2.COLOR_GRAY2RGB)

        return dilated_4x4_rgb, dilated_7x7_rgb
