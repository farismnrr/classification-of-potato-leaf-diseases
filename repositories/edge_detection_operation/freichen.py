import numpy as np

class FreiChenEdgeDetector:
    def __init__(self):
        self.sqrt2 = np.sqrt(2)
        self.kernel_1 = np.array([[1, self.sqrt2, 1],
                                 [0, 0, 0], 
                                 [-1, -self.sqrt2, -1]])
        
        self.kernel_2 = np.array([[-1, 0, 1],
                                 [-self.sqrt2, 0, self.sqrt2],
                                 [-1, 0, 1]])

    def convolve2d(self, image, kernel):
        i_height, i_width = image.shape
        k_height, k_width = kernel.shape
        
        pad_h = k_height // 2
        pad_w = k_width // 2
        
        padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
        
        output = np.zeros_like(image)
        
        for i in range(i_height):
            for j in range(i_width):
                region = padded[i:i+k_height, j:j+k_width]
                output[i, j] = np.sum(region * kernel)
                
        return output

    def detect_edges(self, image):
        if len(image.shape) == 3:
            grayscale = 0.299 * image[:,:,0] + 0.587 * image[:,:,1] + 0.114 * image[:,:,2]
        else:
            grayscale = image.copy()

        gradient_1 = self.convolve2d(grayscale, self.kernel_1)
        gradient_2 = self.convolve2d(grayscale, self.kernel_2)

        edge_image = np.sqrt(np.square(gradient_1) + np.square(gradient_2))
        
        edge_image = (edge_image / edge_image.max() * 255).astype(np.uint8)
        
        return edge_image
