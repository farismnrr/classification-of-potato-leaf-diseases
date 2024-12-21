import numpy as np
import cv2

class MeanFilter:
    def __init__(self, image):
        self.image = image
        
    def process(self):
        # Convert to grayscale if image is color
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image
            
        rows, cols = gray.shape
        filtered_image = np.zeros((rows, cols), dtype=np.uint8)
        
        for y in range(1, rows-1):
            for x in range(1, cols-1):
                # Ambil 3x3 area di sekitar piksel (termasuk dirinya sendiri)
                neighbors = [
                    gray[y-1, x-1], gray[y-1, x], gray[y-1, x+1],
                    gray[y, x-1], gray[y, x], gray[y, x+1],
                    gray[y+1, x-1], gray[y+1, x], gray[y+1, x+1]
                ]
                # Hitung mean (rata-rata) dari tetangga
                mean_value = np.mean(neighbors)
                filtered_image[y, x] = mean_value
        
        return filtered_image