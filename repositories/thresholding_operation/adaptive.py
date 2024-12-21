import numpy as np

class AdaptiveThresholding:
    def __init__(self, image, block_size=11, c=2):
        if len(image.shape) == 3:
            self.image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            self.image = image
        self.block_size = block_size
        self.c = c
        self.height, self.width = self.image.shape

    def process(self):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)
        
        # Create output binary image
        binary = np.zeros_like(self.image)
        
        # Pad image to handle borders
        pad = self.block_size // 2
        padded_img = np.pad(self.image, pad, mode='reflect')
        
        # Apply adaptive thresholding
        for i in range(self.height):
            for j in range(self.width):
                # Extract local window
                window = padded_img[i:i+self.block_size, j:j+self.block_size]
                
                # Calculate local mean
                threshold = np.mean(window) - self.c
                
                # Apply threshold
                if self.image[i,j] > threshold:
                    binary[i,j] = 255
                else:
                    binary[i,j] = 0
                    
        return binary

    def mean(self):
        return self.process()
        
    def gaussian(self):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)
        
        # Create output binary image
        binary = np.zeros_like(self.image)
        
        # Create Gaussian kernel
        pad = self.block_size // 2
        y, x = np.ogrid[-pad:pad+1, -pad:pad+1]
        gaussian = np.exp(-(x*x + y*y)/(2*(pad/2)**2))
        gaussian = gaussian / gaussian.sum()
        
        # Pad image
        padded_img = np.pad(self.image, pad, mode='reflect')
        
        # Apply adaptive thresholding with Gaussian weights
        for i in range(self.height):
            for j in range(self.width):
                # Extract local window
                window = padded_img[i:i+self.block_size, j:j+self.block_size]
                
                # Calculate weighted mean
                threshold = np.sum(window * gaussian) - self.c
                
                # Apply threshold
                if self.image[i,j] > threshold:
                    binary[i,j] = 255
                else:
                    binary[i,j] = 0
                    
        return binary
