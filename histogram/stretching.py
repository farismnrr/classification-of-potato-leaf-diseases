import numpy as np
import cv2
import matplotlib.pyplot as plt

# Rumus Histogram Stretching
# baru(x,y) = lama(x,y) - γmax / γmin - γmax * 255

img = cv2.imread('stretching.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gamma_min = np.min(img)
gamma_max = np.max(img)

stretched_img = (img - gamma_min) / (gamma_max - gamma_min) * 255
stretched_img = stretched_img.astype(np.uint8)

height, width = img.shape
n = height * width
L = 256

histogram_asli = np.zeros(L)
for i in range(L):
    ni = np.sum(img == i)
    histogram_asli[i] = ni / n

histogram_stretched = np.zeros(L)
for i in range(L):
    ni = np.sum(stretched_img == i)
    histogram_stretched[i] = ni / n

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')

plt.figure()
plt.imshow(stretched_img, cmap='gray')
plt.title('Hasil Histogram Stretching')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(range(L), histogram_asli, width=1)
plt.title('Histogram Sebelum Stretching')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Probabilitas')

plt.subplot(1, 2, 2)
plt.bar(range(L), histogram_stretched, width=1)
plt.title('Histogram Setelah Stretching')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Probabilitas')

plt.show()
