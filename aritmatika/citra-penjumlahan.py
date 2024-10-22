import cv2
import numpy as np

image1 = cv2.imread("tom.png") 
image2 = cv2.imread("jerry.png") 

image1 = cv2.resize(image1, (512, 512))
image2 = cv2.resize(image2, (512, 512))

def addition(A, B, C, N, M):
    for i in range(N):
        for j in range(M):
            temp = A[i][j] + B[i][j]
            if temp > 255:
                C[i][j] = 255
            else:
                C[i][j] = temp

N, M, _ = image1.shape

result_image = np.zeros((N, M, 3), dtype=np.uint8)


for channel in range(3):  
    addition(image1[:, :, channel], image2[:, :, channel], result_image[:, :, channel], N, M)


cv2.imshow("Image 1 - Tom", image1)
cv2.imshow("Image 2 - Jerry", image2)
cv2.imshow("Image Addition - Tom and Jerry", result_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
