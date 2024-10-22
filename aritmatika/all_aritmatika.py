import cv2
import numpy as np

# Bagian 1: Perkalian Gambar Grayscale
image_A = cv2.imread('Tom_and_jerry.png', cv2.IMREAD_GRAYSCALE)  # Membaca gambar A dalam grayscale
image_B = cv2.imread('jerry.png', cv2.IMREAD_GRAYSCALE)  # Membaca gambar B dalam grayscale

M, N = image_A.shape  # Mendapatkan dimensi gambar
result_image_mult = np.zeros((M, N), dtype=np.uint8)  # Membuat gambar hasil perkalian

def multiplication(A, B, C, M, N):
    for i in range(M):
        for j in range(N):
            C[i, j] = A[i, j] * B[i, j]  # Mengalikan piksel
            if C[i, j] < 0:
                C[i, j] = 0  # Menghindari nilai negatif
            elif C[i, j] > 255:
                C[i, j] = 255  # Menghindari nilai lebih dari 255

multiplication(image_A, image_B, result_image_mult, M, N)  # Melakukan operasi perkalian

# Menampilkan hasil perkalian
cv2.imshow("Multiplied Image", result_image_mult)

# Bagian 2: Penjumlahan Gambar Berwarna
image1 = cv2.imread("tom.png")  # Membaca gambar 1
image2 = cv2.imread("jerry.png")  # Membaca gambar 2

image1 = cv2.resize(image1, (512, 512))  # Mengubah ukuran gambar 1
image2 = cv2.resize(image2, (512, 512))  # Mengubah ukuran gambar 2

def addition(A, B, C, N, M):
    for i in range(N):
        for j in range(M):
            temp = A[i][j] + B[i][j]  # Menjumlahkan piksel
            if temp > 255:
                C[i][j] = 255  # Menghindari nilai lebih dari 255
            else:
                C[i][j] = temp  # Menyimpan nilai hasil penjumlahan

N, M, _ = image1.shape  # Mendapatkan dimensi gambar berwarna
result_image_add = np.zeros((N, M, 3), dtype=np.uint8)  # Membuat gambar hasil penjumlahan

for channel in range(3):  # Melakukan penjumlahan untuk setiap saluran warna
    addition(image1[:, :, channel], image2[:, :, channel], result_image_add[:, :, channel], N, M)

# Menampilkan hasil penjumlahan
cv2.imshow("Image 1 - Tom", image1)
cv2.imshow("Image 2 - Jerry", image2)
cv2.imshow("Added Image - Tom and Jerry", result_image_add)

# Bagian 3: Pengurangan Gambar Berwarna
image_with_object = cv2.imread('tom_and_jerry.png')  # Membaca gambar dengan objek
image_without_object = cv2.imread('tom.png')  # Membaca gambar tanpa objek

M, N, _ = image_with_object.shape  # Mendapatkan dimensi gambar
result_image_sub = np.zeros((M, N, 3), dtype=np.uint8)  # Membuat gambar hasil pengurangan

def subtraction(A, B, C, M, N):
    for i in range(M):
        for j in range(N):
            for k in range(3):  # Mengiterasi saluran warna (B, G, R)
                diff = int(A[i, j, k]) - int(B[i, j, k])  # Mengurangi piksel
                C[i, j, k] = max(0, min(255, diff))  # Menghindari nilai di luar rentang [0, 255]

# Melakukan operasi pengurangan
subtraction(image_with_object, image_without_object, result_image_sub, M, N)

# Menampilkan hasil pengurangan
cv2.imshow("Subtracted Image", result_image_sub)

cv2.waitKey(0)  # Menunggu hingga tombol ditekan
cv2.destroyAllWindows()  # Menutup semua jendela gambar
