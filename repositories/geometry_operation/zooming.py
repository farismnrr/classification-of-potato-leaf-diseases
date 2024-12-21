import numpy as np

class ZoomingGeometry:
    def __init__(self, image):
        self.image = image
        self.rows, self.cols, self.channels = image.shape
        
    def process(self, zoom_factor):
        new_rows = int(self.rows * zoom_factor)
        new_cols = int(self.cols * zoom_factor)
        zoomed_image = np.zeros((new_rows, new_cols, self.channels), dtype=np.uint8)

        for i in range(new_rows):
            for j in range(new_cols):
                old_x = int(i / zoom_factor)
                old_y = int(j / zoom_factor)
                if 0 <= old_x < self.rows and 0 <= old_y < self.cols:
                    zoomed_image[i, j] = self.image[old_x, old_y]

        return zoomed_image