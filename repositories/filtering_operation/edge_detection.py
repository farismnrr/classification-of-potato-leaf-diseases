import numpy as np
import cv2

class EdgeDetectionFilter:
    def __init__(self, image):
        self.image = image
        self.kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        self.kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    def process(self):
        grad_x = cv2.filter2D(self.image, cv2.CV_32F, self.kernel_x)
        grad_y = cv2.filter2D(self.image, cv2.CV_32F, self.kernel_y)
        
        edges = cv2.magnitude(grad_x, grad_y)
        edges = cv2.convertScaleAbs(edges)
        return edges
