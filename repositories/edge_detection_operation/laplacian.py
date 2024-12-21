import numpy as np

class LaplacianEdgeDetector:
    def __init__(self):
        self.kernel = np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])
    
    def detect(self, image):
        if len(image.shape) == 3:
            grayscale = 0.299 * image[:,:,0] + 0.587 * image[:,:,1] + 0.114 * image[:,:,2]
        else:
            grayscale = image.copy()

        rows, cols = grayscale.shape
        edge_image = np.zeros_like(grayscale)
        padded = np.pad(grayscale, ((1,1), (1,1)), mode='constant')
    
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                patch = padded[i-1:i+2, j-1:j+2]
                edge_image[i-1,j-1] = np.sum(patch * self.kernel)
    
        edge_image = np.abs(edge_image)
        edge_image = (edge_image / edge_image.max() * 255).astype(np.uint8)
    
        return edge_image
