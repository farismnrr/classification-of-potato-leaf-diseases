import cv2
import numpy as np

cat_image = cv2.imread("cat.png")
brightness_factor = 50

row = len(cat_image)
col = len(cat_image[0])

b = cat_image[:, :, 0]
g = cat_image[:, :, 1]
r = cat_image[:, :, 2]

brightened_b = np.zeros((row, col), dtype=np.uint8)
brightened_g = np.zeros((row, col), dtype=np.uint8)
brightened_r = np.zeros((row, col), dtype=np.uint8)

for i in range(row):
    for j in range(col):
        temp_b = b[i, j] + brightness_factor
        if temp_b > 255:
            brightened_b[i, j] = 255
        else:
            brightened_b[i, j] = temp_b
        
        temp_g = g[i, j] + brightness_factor
        if temp_g > 255:
            brightened_g[i, j] = 255
        else:
            brightened_g[i, j] = temp_g
        
        temp_r = r[i, j] + brightness_factor
        if temp_r > 255:
            brightened_r[i, j] = 255
        else:
            brightened_r[i, j] = temp_r

brightened_cat_image = cv2.merge((brightened_b, brightened_g, brightened_r))

cv2.imshow("Original Cat Image", cat_image)
cv2.imshow("Brightened Cat Image", brightened_cat_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
