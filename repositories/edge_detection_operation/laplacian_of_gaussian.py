import numpy as np

class LaplacianOfGaussianEdgeDetection:
    def __init__(self, image):
        self.image = image
        self.sigma = 1.4
        self.kernel_size = 5
        self.laplacian_kernel = np.array([[0, 1, 0],
                                         [1, -4, 1],
                                         [0, 1, 0]])

    def process(self):
        if len(self.image.shape) == 3:
            grayscale = 0.299 * self.image[:,:,0] + 0.587 * self.image[:,:,1] + 0.114 * self.image[:,:,2]
        else:
            grayscale = self.image.copy()

        kernel = np.zeros((self.kernel_size, self.kernel_size))
        center = self.kernel_size // 2
        
        for i in range(self.kernel_size):
            for j in range(self.kernel_size):
                x = i - center
                y = j - center
                kernel[i,j] = (1/(2*np.pi*self.sigma**2)) * np.exp(-(x**2 + y**2)/(2*self.sigma**2))
        
        kernel = kernel / np.sum(kernel)

        rows, cols = grayscale.shape
        blurred = np.zeros_like(grayscale)
        pad_size = self.kernel_size // 2
        
        padded = np.pad(grayscale, pad_size, mode='reflect')
        
        for i in range(rows):
            for j in range(cols):
                window = padded[i:i+self.kernel_size, j:j+self.kernel_size]
                blurred[i,j] = np.sum(window * kernel)

        rows, cols = blurred.shape
        laplacian = np.zeros_like(blurred)
        pad_size = 1
        
        padded = np.pad(blurred, pad_size, mode='reflect')
        
        for i in range(rows):
            for j in range(cols):
                window = padded[i:i+3, j:j+3]
                laplacian[i,j] = np.sum(window * self.laplacian_kernel)
        
        edge_image = np.abs(laplacian)
        edge_image = (edge_image / edge_image.max() * 255).astype(np.uint8)
        
        return edge_image
