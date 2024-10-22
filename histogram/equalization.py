import numpy as np
import cv2
import matplotlib.pyplot as plt

# Histogram Equalization
# 
# Ko = round(Ci * ((2^k) - 1)) / w * h
# 
# Ci: Distribusi kumulatif dari nilai skala keabuan ke-i dari citra asli
# round: Fungsi pembulatan ke bilangan yang terdekat
# Ko: nilai keabuan hasil histogram equalization
# w: lebar citra
# h: tinggi citra

img = cv2.imread('equalization.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = img.shape
n = height * width 
L = 256

histogram_asli = np.zeros(L)
for i in range(L):
    histogram_asli[i] = np.sum(img == i)

histogram_normalisasi = histogram_asli / n

CDF_manual = np.zeros(L)
CDF_manual[0] = histogram_normalisasi[0]
for i in range(1, L):
    CDF_manual[i] = CDF_manual[i - 1] + histogram_normalisasi[i]

k = 8
Ko = np.round(CDF_manual * ((2 ** k) - 1))

equalized_img = np.zeros_like(img)
for i in range(height):
    for j in range(width):
        equalized_img[i, j] = Ko[img[i, j]]

histogram_equalized = np.zeros(L)
for i in range(L):
    histogram_equalized[i] = np.sum(equalized_img == i)

histogram_equalized_normalized = histogram_equalized / n

plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')

plt.figure()
plt.imshow(equalized_img, cmap='gray')
plt.title('Hasil Histogram Equalization')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(range(L), histogram_normalisasi, width=1)
plt.title('Histogram Sebelum Equalization')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Probabilitas')

plt.subplot(1, 2, 2)
plt.bar(range(L), histogram_equalized_normalized, width=1)
plt.title('Histogram Setelah Equalization')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Probabilitas')

# Tampilkan semua plot
plt.show()
