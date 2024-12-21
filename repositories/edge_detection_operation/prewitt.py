import numpy as np

class PrewittEdgeDetection:
    def __init__(self, image):
        self.image = image
        self.kernel_x = np.array([[-1, 0, 1],
                                 [-1, 0, 1],
                                 [-1, 0, 1]])
        
        self.kernel_y = np.array([[-1, -1, -1],
                                 [0, 0, 0], 
                                 [1, 1, 1]])

    def process(self):
        if len(self.image.shape) == 3:
            grayscale = 0.299 * self.image[:,:,0] + 0.587 * self.image[:,:,1] + 0.114 * self.image[:,:,2]
        else:
            grayscale = self.image.copy()

        height, width = grayscale.shape
        gradient_x = np.zeros_like(grayscale)
        gradient_y = np.zeros_like(grayscale)
        
        for i in range(1, height-1):
            for j in range(1, width-1):
                neighborhood = grayscale[i-1:i+2, j-1:j+2]
                gradient_x[i,j] = np.sum(neighborhood * self.kernel_x)
                gradient_y[i,j] = np.sum(neighborhood * self.kernel_y)

        edge_image = np.sqrt(np.square(gradient_x) + np.square(gradient_y))
        edge_image = (edge_image / edge_image.max() * 255).astype(np.uint8)
        
        return edge_image
