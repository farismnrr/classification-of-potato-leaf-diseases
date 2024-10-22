import cv2
import numpy as np

# Fungsi untuk filter median manual (sudah diberikan)
def median_filter_manual(image):
    rows, cols = image.shape
    filtered_image = np.zeros((rows, cols), dtype=np.uint8)
    
    # Ambil 3x3 area di sekitar piksel (termasuk dirinya sendiri)
    for y in range(1, rows-1):
        for x in range(1, cols-1):
            neighbors = [
                image[y-1, x-1], image[y-1, x], image[y-1, x+1],
                image[y, x-1], image[y, x], image[y, x+1],
                image[y+1, x-1], image[y+1, x], image[y+1, x+1]
            ]
            median_value = np.median(neighbors)
            filtered_image[y, x] = median_value
    
    return filtered_image

# Fungsi untuk filter mean (rata-rata)
def mean_filter_manual(image):
    rows, cols = image.shape
    filtered_image = np.zeros((rows, cols), dtype=np.uint8)
    
    for y in range(1, rows-1):
        for x in range(1, cols-1):
            # Ambil 3x3 area di sekitar piksel (termasuk dirinya sendiri)
            neighbors = [
                image[y-1, x-1], image[y-1, x], image[y-1, x+1],
                image[y, x-1], image[y, x], image[y, x+1],
                image[y+1, x-1], image[y+1, x], image[y+1, x+1]
            ]
            # Hitung mean (rata-rata) dari tetangga
            mean_value = np.mean(neighbors)
            filtered_image[y, x] = mean_value
    
    return filtered_image

# Fungsi untuk filter batas (deteksi tepi)
def edge_detection_filter(image):
    # Kernel Sobel untuk deteksi tepi horizontal dan vertikal
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    # Konvolusi dengan kernel Sobel
    grad_x = cv2.filter2D(image, cv2.CV_32F, kernel_x)  # Ubah tipe data ke float
    grad_y = cv2.filter2D(image, cv2.CV_32F, kernel_y)  # Ubah tipe data ke float
    
    # Kombinasikan gradien X dan Y untuk mendapatkan magnitudo
    edges = cv2.magnitude(grad_x, grad_y)
    edges = cv2.convertScaleAbs(edges)  # Ubah kembali ke uint8 untuk ditampilkan atau disimpan
    return edges


# Fungsi untuk filter perataan (lowpass)
def lowpass_filter(image):
    kernel = np.ones((3, 3), np.float32) / 9
    smoothed = cv2.filter2D(image, -1, kernel)
    return smoothed

# Fungsi untuk filter highpass
def highpass_filter(image):
    # Kernel highpass sederhana rumus 3x3 * 1/9
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    highpass = cv2.filter2D(image, -1, kernel)
    return highpass

# Baca gambar grayscale
image = cv2.imread('test.jpeg', cv2.IMREAD_GRAYSCALE)

# Terapkan berbagai jenis filter
median_filtered = median_filter_manual(image)
mean_filtered = mean_filter_manual(image)
edges = edge_detection_filter(image)
smoothed = lowpass_filter(image)
highpass = highpass_filter(image)

# Simpan hasilnya
cv2.imwrite('median_filtered.jpg', median_filtered)
cv2.imwrite('mean_filtered.jpg', mean_filtered)
cv2.imwrite('edges.jpg', edges)
cv2.imwrite('smoothed.jpg', smoothed)
cv2.imwrite('highpass.jpg', highpass)

# Tampilkan hasil sebelum dan sesudah
cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered', median_filtered)
cv2.imshow('Mean Filtered', mean_filtered)
cv2.imshow('batas', edges)
cv2.imshow('Lowpass Filtered', smoothed)
cv2.imshow('Highpass Filtered', highpass)
cv2.waitKey(0)
cv2.destroyAllWindows()
