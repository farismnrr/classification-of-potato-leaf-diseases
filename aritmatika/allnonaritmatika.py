import cv2
import numpy as np

# Bagian pertama: Konversi citra ke grayscale
# Membaca citra
citra = cv2.imread("cat.png")

# Pisahkan komponen warna RGB
b = citra[:, :, 0]
g = citra[:, :, 1]
r = citra[:, :, 2]

# Dapatkan ukuran citra
row = len(citra)
col = len(citra[0])

# Inisialisasi citra grayscale
citra_grayscale = np.zeros((row, col))
print(citra_grayscale)

# Loop untuk konversi setiap piksel ke grayscale
for i in range(row):
    for j in range(col):
        citra_grayscale[i, j] = 0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j]

# Ubah tipe data ke uint8
citra_grayscale = citra_grayscale.astype(np.uint8)

# Tampilkan citra asli dan grayscale
cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Grayscale", citra_grayscale)
print(citra_grayscale)

# Bagian kedua: Penyesuaian kecerahan pada citra asli
# Membaca ulang citra yang sama
cat_image = cv2.imread("cat.png")

# Faktor kecerahan
brightness_factor = 50

# Dapatkan ukuran citra
row = len(cat_image)
col = len(cat_image[0])

# Pisahkan komponen warna RGB
b = cat_image[:, :, 0]
g = cat_image[:, :, 1]
r = cat_image[:, :, 2]

# Inisialisasi array untuk komponen warna setelah kecerahan ditingkatkan
brightened_b = np.zeros((row, col), dtype=np.uint8)
brightened_g = np.zeros((row, col), dtype=np.uint8)
brightened_r = np.zeros((row, col), dtype=np.uint8)

# Loop untuk meningkatkan kecerahan setiap piksel
for i in range(row):
    for j in range(col):
        # Penyesuaian kecerahan untuk channel biru
        temp_b = b[i, j] + brightness_factor
        if temp_b > 255:
            brightened_b[i, j] = 255
        else:
            brightened_b[i, j] = temp_b
        
        # Penyesuaian kecerahan untuk channel hijau
        temp_g = g[i, j] + brightness_factor
        if temp_g > 255:
            brightened_g[i, j] = 255
        else:
            brightened_g[i, j] = temp_g
        
        # Penyesuaian kecerahan untuk channel merah
        temp_r = r[i, j] + brightness_factor
        if temp_r > 255:
            brightened_r[i, j] = 255
        else:
            brightened_r[i, j] = temp_r

# Gabungkan komponen warna yang sudah ditingkatkan kecerahannya
brightened_cat_image = cv2.merge((brightened_b, brightened_g, brightened_r))

# Tampilkan citra asli dan citra dengan kecerahan yang ditingkatkan
cv2.imshow("Brightened Cat Image", brightened_cat_image)

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
        temp_b = b[i, j] - brightness_factor
        if temp_b < 0:
            brightened_b[i, j] = 0
        else:
            brightened_b[i, j] = temp_b
        
        temp_g = g[i, j] - brightness_factor
        if temp_g < 0:
            brightened_g[i, j] = 0
        else:
            brightened_g[i, j] = temp_g
        
        temp_r = r[i, j] - brightness_factor
        if temp_r < 0:
            brightened_r[i, j] = 0
        else:
            brightened_r[i, j] = temp_r

brightened_cat_image = cv2.merge((brightened_b, brightened_g, brightened_r))


cv2.imshow("Citra Pengurangan Skalar", brightened_cat_image)


# Faktor pencerahan
brightness_factor = 50

# Fungsi pencerahan citra sesuai dengan rumus yang diberikan
def image_brightening(A, b, M, N):
    # Buat array citra hasil B dengan ukuran M x N (untuk citra berwarna, tambah channels)
    B = np.zeros((M, N, 3), dtype=np.uint8)

    # Proses pencerahan manual
    for i in range(M):
        for j in range(N):
            for c in range(3):  # 3 karena RGB (3 channels)
                temp = A[i, j, c] + b  # Penambahan skalar b pada tiap piksel
                
                # Clipping
                if temp < 0:
                    B[i, j, c] = 0
                elif temp > 255:
                    B[i, j, c] = 255
                else:
                    B[i, j, c] = temp

    return B

# Dapatkan dimensi citra (M = baris, N = kolom)
M, N, _ = cat_image.shape

# Terapkan fungsi pencerahan
brightened_cat_image = image_brightening(cat_image, brightness_factor, M, N)

# Tampilkan citra asli dan citra yang sudah diterangkan

cv2.imshow("Citra penjumlahan skalar", brightened_cat_image)

brightness_factor = 1.5  # Faktor pembagian kecerahan

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
        temp_b = b[i, j] / brightness_factor
        if temp_b < 0:
            brightened_b[i, j] = 0
        else:
            brightened_b[i, j] = temp_b
        
        temp_g = g[i, j] / brightness_factor
        if temp_g < 0:
            brightened_g[i, j] = 0
        else:
            brightened_g[i, j] = temp_g
        
        temp_r = r[i, j] / brightness_factor
        if temp_r < 0:
            brightened_r[i, j] = 0
        else:
            brightened_r[i, j] = temp_r

brightened_cat_image = cv2.merge((brightened_b, brightened_g, brightened_r))


cv2.imshow("Citra Pembagian skalar", brightened_cat_image)

cat_image = cv2.imread("cat.png")
brightness_factor = 1.5  # Faktor perkalian kecerahan

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
        temp_b = b[i, j] * brightness_factor
        if temp_b > 255:
            brightened_b[i, j] = 255
        else:
            brightened_b[i, j] = temp_b
        
        temp_g = g[i, j] * brightness_factor
        if temp_g > 255:
            brightened_g[i, j] = 255
        else:
            brightened_g[i, j] = temp_g
        
        temp_r = r[i, j] * brightness_factor
        if temp_r > 255:
            brightened_r[i, j] = 255
        else:
            brightened_r[i, j] = temp_r

brightened_cat_image = cv2.merge((brightened_b, brightened_g, brightened_r))


cv2.imshow("Citra Perkalian skalar", brightened_cat_image)
# Tunggu input dari pengguna sebelum menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
