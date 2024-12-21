import numpy as np

class SobelEdgeDetection:
    def __init__(self, image):
        self.image = image
        self.kernel_x = np.array([[-1, 0, 1],
                                 [-2, 0, 2],
                                 [-1, 0, 1]])
        
        self.kernel_y = np.array([[-1, -2, -1],
                                 [0, 0, 0],
                                 [1, 2, 1]])
    
    def process(self):
        if len(self.image.shape) == 3:
            grayscale = 0.299 * self.image[:,:,0] + 0.587 * self.image[:,:,1] + 0.114 * self.image[:,:,2]
        else:
            grayscale = self.image.copy()

        height, width = grayscale.shape
        gradient_x = np.zeros_like(grayscale)
        gradient_y = np.zeros_like(grayscale)
        
        for y in range(1, height-1):
            for x in range(1, width-1):
                neighborhood = grayscale[y-1:y+2, x-1:x+2]
                gradient_x[y,x] = np.sum(neighborhood * self.kernel_x)
                gradient_y[y,x] = np.sum(neighborhood * self.kernel_y)

        edge_image = np.sqrt(np.square(gradient_x) + np.square(gradient_y))
        edge_image = (edge_image / edge_image.max() * 255).astype(np.uint8)
        
        return edge_image
