import cv2
import numpy as np

# Load the images in color
image_with_object = cv2.imread('tom_and_jerry.png')
image_without_object = cv2.imread('tom.png')

# Get the shape of the images (assuming both are the same size)
M, N, _ = image_with_object.shape

# Create an empty array for the result image
result_image = np.zeros((M, N, 3), dtype=np.uint8)

def subtraction(A, B, C, M, N):
    for i in range(M):
        for j in range(N):
            for k in range(3):  # Iterate over the color channels (B, G, R)
                diff = int(A[i, j, k]) - int(B[i, j, k])
                C[i, j, k] = max(0, min(255, diff))  # Clamp values between 0 and 255

# Perform the subtraction
subtraction(image_with_object, image_without_object, result_image, M, N)

# Display the images
cv2.imshow("Image with Object", image_with_object)
cv2.imshow("Image without Object", image_without_object)
cv2.imshow("Subtracted Image", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
