import numpy as np
import math

class CannyEdgeDetector:
    def __init__(self):
        pass
        
    def gaussian_kernel(self, size=5, sigma=1.4):
        kernel = np.zeros((size, size))
        center = size // 2
        
        for i in range(size):
            for j in range(size):
                x, y = i - center, j - center
                kernel[i,j] = (1/(2*np.pi*sigma**2)) * np.exp(-(x**2 + y**2)/(2*sigma**2))
                
        return kernel / kernel.sum()

    def convolve2d(self, image, kernel):
        k_height, k_width = kernel.shape
        pad_h = k_height // 2
        pad_w = k_width // 2
        
        padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
        
        height, width = image.shape
        result = np.zeros_like(image, dtype=np.float64)
        
        for i in range(height):
            for j in range(width):
                result[i,j] = np.sum(padded[i:i+k_height, j:j+k_width] * kernel)
                
        return result

    def process(self, image):
        if len(image.shape) == 3:
            grayscale = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            grayscale = image.copy()

        gaussian = self.gaussian_kernel()
        blurred = self.convolve2d(grayscale, gaussian)
        
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        
        gradient_x = self.convolve2d(blurred, sobel_x)
        gradient_y = self.convolve2d(blurred, sobel_y)
        
        magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
        direction = np.arctan2(gradient_y, gradient_x)
        
        height, width = magnitude.shape
        suppressed = np.zeros_like(magnitude)
        
        direction = direction * 180 / np.pi
        direction[direction < 0] += 180
        
        for i in range(1, height-1):
            for j in range(1, width-1):
                angle = direction[i, j]
                
                if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                    neighbors = [magnitude[i, j-1], magnitude[i, j+1]]
                elif 22.5 <= angle < 67.5:
                    neighbors = [magnitude[i-1, j+1], magnitude[i+1, j-1]]
                elif 67.5 <= angle < 112.5:
                    neighbors = [magnitude[i-1, j], magnitude[i+1, j]]
                else:
                    neighbors = [magnitude[i-1, j-1], magnitude[i+1, j+1]]
                    
                if magnitude[i, j] >= max(neighbors):
                    suppressed[i, j] = magnitude[i, j]
        
        high_threshold = np.max(suppressed) * 0.15
        low_threshold = high_threshold * 0.05
        
        strong_edges = (suppressed >= high_threshold).astype(np.uint8) * 255
        weak_edges = ((suppressed >= low_threshold) & (suppressed < high_threshold)).astype(np.uint8) * 255
        
        final_edges = strong_edges.copy()
        
        weak_y, weak_x = np.where(weak_edges == 255)
        
        for y, x in zip(weak_y, weak_x):
            if np.any(strong_edges[max(0, y-1):min(y+2, height), 
                                  max(0, x-1):min(x+2, width)] == 255):
                final_edges[y, x] = 255
                
        return final_edges