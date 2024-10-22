import cv2
import numpy as np

image_A = cv2.imread('Tom.png', cv2.IMREAD_GRAYSCALE)
image_B = cv2.imread('jerry.png', cv2.IMREAD_GRAYSCALE)

M, N = image_A.shape

result_image = np.zeros((M, N), dtype=np.uint8)

def multiplication(A, B, C, M, N):
    for i in range(M):
        for j in range(N):
            C[i, j] = A[i, j] * B[i, j]
            if C[i, j] < 0:
                C[i, j] = 0
            elif C[i, j] > 255:
                C[i, j] = 255

multiplication(image_A, image_B, result_image, M, N)

cv2.imshow("Image A", image_A)
cv2.imshow("Image B", image_B)
cv2.imshow("Multiplied Image", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
