import numpy as np
import cv2
import matplotlib.pyplot as plt

# Rumus Histogram Normalisasi
# 
# hi = ni/n
# 
# n1: jumlah pixel yang memiliki derajat keabuan i
# n: jumlah seluruh pixel di dalam citra
# i: 0.1, ... L-1

img = cv2.imread('normalise.png', cv2.IMREAD_GRAYSCALE)

height, width = img.shape
n = height * width
L = 256

histogram_asli = np.zeros(L)

for i in range(L):
    ni = np.sum(img == i)
    histogram_asli[i] = ni / n

CDF = np.zeros(L)
CDF[0] = histogram_asli[0]
for i in range(1, L):
    CDF[i] = CDF[i-1] + histogram_asli[i]

CDF_normalized = CDF / CDF.max()

equalized_img = np.zeros_like(img, dtype=np.uint8)
for i in range(height):
    for j in range(width):
        equalized_img[i, j] = np.uint8((L - 1) * CDF_normalized[img[i, j]])

histogram_normalisasi = np.zeros(L)
for i in range(L):
    ni = np.sum(equalized_img == i)
    histogram_normalisasi[i] = ni / n

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')

plt.figure()
plt.imshow(equalized_img, cmap='gray')
plt.title('Gambar Setelah Normalisasi')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(range(L), histogram_asli, width=1)
plt.title('Histogram Sebelum Normalisasi')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Probabilitas')

plt.subplot(1, 2, 2)
plt.bar(range(L), histogram_normalisasi, width=1)
plt.title('Histogram Setelah Normalisasi')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Probabilitas')

plt.show()
