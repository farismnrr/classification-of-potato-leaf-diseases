import numpy as np

class MultiLevelThresholding:
    def __init__(self, image, levels):
        if len(image.shape) == 3:
            self.image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        else:
            self.image = image
        
        # Convert levels to thresholds
        self.levels = levels
        step = 256 // levels
        self.thresholds = [step * i for i in range(1, levels)]  # Create thresholds based on levels
        
        self.height, self.width = self.image.shape

    def process(self):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)
        
        # Create output image
        output = np.zeros_like(self.image)
        
        # Apply multi-level thresholding
        for i in range(len(self.thresholds) + 1):
            if i == 0:
                # First segment (0 to first threshold)
                mask = self.image <= self.thresholds[0]
                output[mask] = 0
            elif i == len(self.thresholds):
                # Last segment (last threshold to 255)
                mask = self.image > self.thresholds[-1]
                output[mask] = 255
            else:
                # Middle segments
                mask = (self.image > self.thresholds[i-1]) & (self.image <= self.thresholds[i])
                output[mask] = int(255 * (i / len(self.thresholds)))
        
        return output

    def otsu_multilevel(self, num_thresholds=2):
        # Convert image to uint8 if not already
        self.image = self.image.astype(np.uint8)
        
        # Calculate histogram
        histogram = np.zeros(256)
        for i in range(256):
            histogram[i] = np.sum(self.image == i)
            
        # Normalize histogram
        histogram = histogram / (self.height * self.width)
        
        # Initialize variables for best thresholds
        max_variance = 0
        best_thresholds = []
        
        # Brute force search for optimal thresholds
        for t1 in range(0, 256-num_thresholds):
            if num_thresholds == 1:
                variance = self._calculate_variance(histogram, [t1])
                if variance > max_variance:
                    max_variance = variance
                    best_thresholds = [t1]
            else:
                for t2 in range(t1+1, 256):
                    variance = self._calculate_variance(histogram, [t1, t2])
                    if variance > max_variance:
                        max_variance = variance
                        best_thresholds = [t1, t2]
        
        # Update thresholds and apply them
        self.thresholds = sorted(best_thresholds)
        return self.process()
    
    def _calculate_variance(self, histogram, thresholds):
        # Helper function to calculate between-class variance for multiple thresholds
        thresholds = [-1] + sorted(thresholds) + [255]
        means = []
        weights = []
        
        # Calculate means and weights for each segment
        for i in range(len(thresholds)-1):
            start = thresholds[i] + 1
            end = thresholds[i+1] + 1
            
            segment_hist = histogram[start:end]
            weight = np.sum(segment_hist)
            
            if weight == 0:
                means.append(0)
            else:
                mean = np.sum(np.arange(start, end) * segment_hist) / weight
                means.append(mean)
            weights.append(weight)
        
        # Calculate global mean
        global_mean = np.sum(np.arange(256) * histogram)
        
        # Calculate between-class variance
        variance = 0
        for w, m in zip(weights, means):
            if w > 0:
                variance += w * ((m - global_mean) ** 2)
                
        return variance
