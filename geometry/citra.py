import cv2
from operations import translation
from operations import rotation
from operations import flipping
from operations import zooming

def print_image_matrix(image):
    print("\nMatriks piksel:")
    for row in image:
        print(" ".join(str(pixel[0]) for pixel in row))

img = cv2.imread('cat.png')

if img is None:
    print("Gambar tidak ditemukan. Pastikan 'cat.png' berada di folder yang benar.")
    exit()

while True:
    print("\nPilih operasi geometri:")
    print("1. Translasi")
    print("2. Rotasi")
    print("3. Flipping")
    print("4. Zooming")
    print("5. Keluar")

    choice = input("Masukkan pilihan (1-5): ")

    if choice == '1':  # Translate
        shift_x = int(input("Masukkan nilai translasi untuk sumbu X: "))
        shift_y = int(input("Masukkan nilai translasi untuk sumbu Y: "))
        translated_img = translation.translate(img, shift_x, shift_y)
        cv2.imshow("Translasi", translated_img)
    
    elif choice == '2':  # Rotate
        angle = float(input("Masukkan sudut rotasi (derajat): "))
        rotated_img = rotation.rotate(img, angle)
        cv2.imshow("Rotasi", rotated_img)
    
    elif choice == '3':  # Flip
        print("Pilihan flipping: 1 (Horizontal), 0 (Vertical), -1 (Keduanya)")
        flip_code = int(input("Masukkan kode flipping: "))
        flipped_img = flipping.flip(img, flip_code)
        cv2.imshow("Flipping", flipped_img)

    elif choice == '4':  # Zoom
        zoom_factor = float(input("Masukkan faktor zoom (misal: 1.5 untuk zoom in, 0.5 untuk zoom out): "))
        zoomed_img = zooming.zoom(img, zoom_factor)
        cv2.imshow("Zooming", zoomed_img)

    elif choice == '5':  # Keluar
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
