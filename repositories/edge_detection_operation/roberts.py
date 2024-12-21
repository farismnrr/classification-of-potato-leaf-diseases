import numpy as np

class RobertsEdgeDetection:
    def __init__(self, image):
        self.image = image
    
    def process(self):
        if len(self.image.shape) == 3:
            grayscale = np.zeros((self.image.shape[0], self.image.shape[1]))
            for i in range(self.image.shape[0]):
                for j in range(self.image.shape[1]):
                    grayscale[i,j] = 0.299 * self.image[i,j,0] + 0.587 * self.image[i,j,1] + 0.114 * self.image[i,j,2]
        else:
            grayscale = self.image.copy()
        
        height, width = grayscale.shape
        edge_image = np.zeros((height, width))
        
        for y in range(height-1):
            for x in range(width-1):
                gx = grayscale[y, x] - grayscale[y+1, x+1]
                gy = grayscale[y, x+1] - grayscale[y+1, x]
                edge_image[y,x] = np.sqrt(gx**2 + gy**2)
        
        max_val = np.max(edge_image)
        if max_val > 0:
            edge_image = (edge_image / max_val * 255)
        edge_image = edge_image.astype(np.uint8)
        
        return edge_image
