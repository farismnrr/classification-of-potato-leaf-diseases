import numpy as np

def zoom(image, zoom_factor):
    rows, cols, channels = image.shape
    new_rows = int(rows * zoom_factor)
    new_cols = int(cols * zoom_factor)
    zoomed_image = np.zeros((new_rows, new_cols, channels), dtype=np.uint8)

    for i in range(new_rows):
        for j in range(new_cols):
            old_x = int(i / zoom_factor)
            old_y = int(j / zoom_factor)
            if 0 <= old_x < rows and 0 <= old_y < cols:
                zoomed_image[i, j] = image[old_x, old_y]

    return zoomed_image