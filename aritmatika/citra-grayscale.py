import cv2
import numpy as np

citra = cv2.imread("cat.png")

b = citra[:, :, 0]
g = citra[:, :, 1]
r = citra[:, :, 2]

row = len(citra)
col = len(citra[0])

citra_grayscale = np.zeros((row, col))
print(citra_grayscale)

for i in range(row):
    for j in range(col):
        citra_grayscale[i, j] = 0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j]

citra_grayscale = citra_grayscale.astype(np.uint8)

cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Grayscale", citra_grayscale)
print(citra_grayscale)
cv2.waitKey()
cv2.destroyAllWindows()

