import os
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def log_window_size(window, log_text):
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width, screen_height = get_screen_size()
    add_log(log_text, f"Screen resolution: {screen_width}x{screen_height} pixels")
    add_log(log_text, f"Window size: {window_width}x{window_height} pixels")

def validate_image(image_path):
    if not os.path.exists(image_path):
        raise ValueError("File does not exist")
        
    _, file_extension = os.path.splitext(image_path)
    if file_extension.lower() not in ['.png', '.jpg', '.jpeg', '.bmp']:
        raise ValueError("File must be an image (PNG, JPG, JPEG, or BMP)")
        
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read the image")
        
    return img

def add_log(log_text, message):
    log_text.configure(state='normal')
    log_text.insert('end', message + '\n')
    log_text.configure(state='disabled')
    log_text.see('end')

def load_image(loaded_images, key, log_text):
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            # Get image dimensions and size
            img = cv2.imread(file_path)
            height, width = img.shape[:2]
            file_size = os.path.getsize(file_path) / 1024  # Get size in KB
            
            # Load and display image
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            loaded_images[key]['photo'] = photo
            loaded_images[key]['path'] = file_path
            
            # Log image info
            filename = os.path.basename(file_path)
            add_log(log_text, f"Loaded {filename} ({width}x{height} pixels, {file_size:.1f} KB)")
            
            return True
        except Exception as e:
            add_log(log_text, f"Error loading image: {e}")
            return False
    return False
