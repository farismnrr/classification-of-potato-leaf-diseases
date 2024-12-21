import numpy as np

class GradientEdgeDetector:
    def __init__(self):
        pass
        
    def detect(self, image):
        if len(image.shape) == 3:
            grayscale = 0.299 * image[:,:,0] + 0.587 * image[:,:,1] + 0.114 * image[:,:,2]
        else:
            grayscale = image.copy()
        
        height, width = grayscale.shape
        edge_image = np.zeros((height, width))
        
        for y in range(1, height-1):
            for x in range(1, width-1):
                gx = grayscale[y, x+1] - grayscale[y, x-1]  
                gy = grayscale[y+1, x] - grayscale[y-1, x] 
                edge_image[y, x] = np.sqrt(gx**2 + gy**2)
        
        edge_image = (edge_image / np.max(edge_image) * 255).astype(np.uint8)
        
        return edge_image
