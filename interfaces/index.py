import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from utils.index import add_log, load_image, log_window_size
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import platform

class ImageProcessingGUI:
    def __init__(self, general_service, arithmetic_service, geometry_service, histogram_service, filtering_service, morphology_service, edge_detection_service, thresholding_service):    
        self.root = tk.Tk()
        self.root.title("Kelompok 13 - Tugas Pengolahan Citra Digital")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.resizable(True, True)
        
        system = platform.system().lower()
        if system == "windows":
            self.root.state('zoomed')
        elif system == "linux":
            self.root.attributes('-zoomed', True)
        elif system == "darwin": 
            self.root.attributes('-fullscreen', True)
        
        self.root.bind('<Escape>', lambda event: self.root.attributes('-fullscreen', False))

        self.general_service = general_service
        self.arithmetic_service = arithmetic_service
        self.geometry_service = geometry_service
        self.histogram_service = histogram_service
        self.filtering_service = filtering_service
        self.morphology_service = morphology_service
        self.edge_detection_service = edge_detection_service
        self.thresholding_service = thresholding_service
        
        self.log_frame = ttk.Frame(self.root)
        self.log_frame.pack(side="bottom", fill="x", padx=5, pady=5)
        
        self.log_text = tk.Text(self.log_frame, height=8, state='disabled')
        self.log_text.pack(fill="x", expand=True, side="left")
        
        self.log_scrollbar = ttk.Scrollbar(self.log_frame, orient="vertical", command=self.log_text.yview)
        self.log_scrollbar.pack(side="right", fill="y")
        self.log_text.configure(yscrollcommand=self.log_scrollbar.set)

        self.root.update()
        log_window_size(self.root, self.log_text)

        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)

        self.content_canvas = tk.Canvas(self.main_container)
        self.content_canvas.pack(side="left", fill="both", expand=True)

        self.content_scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.content_canvas.yview)
        self.content_scrollbar.pack(side="right", fill="y")
        self.content_canvas.configure(yscrollcommand=self.content_scrollbar.set)

        self.content_frame = ttk.Frame(self.content_canvas)
        self.content_canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        self.main_content = ttk.Frame(self.content_frame)
        self.main_content.pack(fill="both", expand=True)

        self.fixed_frame = ttk.Frame(self.main_content, padding="20")
        self.fixed_frame.pack(fill="x", padx=5, pady=5)

        self.image_frame = ttk.Frame(self.main_content)
        self.image_frame.pack(fill="both", expand=True, pady=10)
        
        self.image_label = ttk.Label(self.image_frame)
        self.image_label.pack(expand=True)

        self.selection_label = ttk.Label(
            self.fixed_frame,
            text="Please select main option:",
            font=("Helvetica", 10)
        )
        self.selection_label.pack(fill="x", padx=5, pady=5)

        self.main_options = ["General Operation", "Arithmetic Operation", "Geometry Operation", "Histogram Operation", "Filtering Operation", "Morphology Operation", "Edge Detection Operation", "Thresholding Operation"]
        self.selected_main_option = tk.StringVar()
        
        self.sub_selection_label = ttk.Label(
            self.fixed_frame,
            text="Please select sub-option:",
            font=("Helvetica", 10)
        )
        
        self.selected_sub_option = tk.StringVar()
        self.sub_dropdown = ttk.Combobox(
            self.fixed_frame,
            textvariable=self.selected_sub_option,
            state="readonly"
        )
        
        self.threshold_frame = ttk.Frame(self.fixed_frame)
        self.threshold_label = ttk.Label(
            self.threshold_frame,
            text="Threshold value (0-255):",
            font=("Helvetica", 10)
        )
        self.threshold_entry = ttk.Entry(self.threshold_frame)
        self.threshold_entry.insert(0, "255")

        self.brightness_frame_addition_subtraction = ttk.Frame(self.fixed_frame)
        self.brightness_label_addition_subtraction = ttk.Label(
            self.brightness_frame_addition_subtraction,
            text="Brightness value (0-255):",
            font=("Helvetica", 10)
        )
        self.brightness_entry_addition_subtraction = ttk.Entry(self.brightness_frame_addition_subtraction)
        self.brightness_entry_addition_subtraction.insert(0, "50")
        
        self.brightness_frame_multiplication_division = ttk.Frame(self.fixed_frame)
        self.brightness_label_multiplication_division = ttk.Label(
            self.brightness_frame_multiplication_division,
            text="Brightness value (0-25):",
            font=("Helvetica", 10)
        )
        self.brightness_entry_multiplication_division = ttk.Entry(self.brightness_frame_multiplication_division)
        self.brightness_entry_multiplication_division.insert(0, "2")

        self.angle_frame = ttk.Frame(self.fixed_frame)
        self.angle_label = ttk.Label(
            self.angle_frame,
            text="Rotation angle (0-360):",
            font=("Helvetica", 10)
        )
        self.angle_entry = ttk.Entry(self.angle_frame)
        self.angle_entry.insert(0, "90")

        self.flip_frame = ttk.Frame(self.fixed_frame)
        self.flip_label = ttk.Label(
            self.flip_frame,
            text="Flip code (-1, 0, 1):",
            font=("Helvetica", 10)
        )
        self.flip_entry = ttk.Entry(self.flip_frame)
        self.flip_entry.insert(0, "1")

        self.zoom_frame = ttk.Frame(self.fixed_frame)
        self.zoom_label = ttk.Label(
            self.zoom_frame,
            text="Zoom factor (0-3):",
            font=("Helvetica", 10)
        )
        self.zoom_entry = ttk.Entry(self.zoom_frame)
        self.zoom_entry.insert(0, "2")

        self.translation_frame = ttk.Frame(self.fixed_frame)
        self.shift_x_label = ttk.Label(
            self.translation_frame,
            text="Shift X:",
            font=("Helvetica", 10)
        )
        self.shift_x_entry = ttk.Entry(self.translation_frame)
        self.shift_x_entry.insert(0, "10")
        self.shift_y_label = ttk.Label(
            self.translation_frame,
            text="Shift Y:",
            font=("Helvetica", 10)
        )
        self.shift_y_entry = ttk.Entry(self.translation_frame)
        self.shift_y_entry.insert(0, "10")
        
        self.global_threshold_frame = ttk.Frame(self.fixed_frame)
        self.global_threshold_label = ttk.Label(
            self.global_threshold_frame,
            text="Global threshold value (0-255):",
            font=("Helvetica", 10)
        )
        self.global_threshold_entry = ttk.Entry(self.global_threshold_frame)
        self.global_threshold_entry.insert(0, "127")

        self.multi_level_frame = ttk.Frame(self.fixed_frame)
        self.multi_level_label = ttk.Label(
            self.multi_level_frame,
            text="Number of levels (2-4):",
            font=("Helvetica", 10)
        )
        self.multi_level_entry = ttk.Entry(self.multi_level_frame)
        self.multi_level_entry.insert(0, "3")

        self.sub_options = {
            "General Operation": [
                "Negative Image", 
                "Grayscale Image", 
                "Brightening Image"
            ],
            "Arithmetic Operation": [
                "Addition Image",
                "Subtraction Image",
                "Multiplication Image",
                "Scalar Addition Image",
                "Scalar Subtraction Image", 
                "Scalar Multiplication Image",
                "Scalar Division Image"
            ],
            "Geometry Operation": [
                "Flipping Image",
                "Rotation Image",
                "Translation Image",
                "Zooming Image"
            ],
            "Histogram Operation": [
                "Equalization",
                "Normalization",
                "Stretching"
            ],
            "Filtering Operation": [
                "Edge Detection",
                "Highpass",
                "Lowpass",
                "Mean",
                "Median"
            ],
            "Morphology Operation": [
                "Opening",
                "Closing",
                "Erosion",
                "Dilation"
            ],
            "Edge Detection Operation": [
                "Canny Edge Detection",
                "Frei-Chen Edge Detection",
                "Gradient Edge Detection",
                "Laplacian Edge Detection",
                "Laplacian of Gaussian Edge Detection",
                "Prewitt Edge Detection",
                "Roberts Edge Detection",
                "Sobel Edge Detection"
            ],
            "Thresholding Operation": [
                "Adaptive Thresholding",
                "Otsu Thresholding",
                "Multi-Level Thresholding",
                "Global Thresholding"
            ]
        }

        self.loaded_images = {
            'image1': {'photo': None, 'path': None},
            'image2': {'photo': None, 'path': None}
        }

        self.load_button1 = ttk.Button(
            self.fixed_frame,
            text="Load Image",
            command=lambda: load_image(self.loaded_images, 'image1', self.log_text),
            style="Submit.TButton"
        )

        self.load_button2 = ttk.Button(
            self.fixed_frame,
            text="Load Image 2", 
            command=lambda: load_image(self.loaded_images, 'image2', self.log_text),
            style="Submit.TButton"
        )

        self.submit_button = ttk.Button(
            self.fixed_frame,
            text="Submit",
            command=self.handle_selection,
            style="Submit.TButton"
        )

        self.main_dropdown = ttk.Combobox(
            self.fixed_frame,
            textvariable=self.selected_main_option,
            values=self.main_options,
            state="readonly"
        )
        self.main_dropdown.pack(fill="x", padx=5, pady=5)
        self.main_dropdown.set("Select main option")
        
        self.selected_main_option.trace('w', self.update_sub_dropdown)

        style = ttk.Style()
        style.configure("Submit.TButton", padding=5)

        self.content_frame.bind("<Configure>", lambda e: self.content_canvas.configure(scrollregion=self.content_canvas.bbox("all")))
        self.content_canvas.bind("<Configure>", self.on_canvas_configure)
        self.content_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_canvas_configure(self, event):
        self.content_canvas.configure(scrollregion=self.content_canvas.bbox("all"))
        self.content_canvas.itemconfig(self.content_canvas.find_withtag("all")[0], width=event.width)

    def update_sub_dropdown(self, *args):
        selected = self.selected_main_option.get()
        if selected != "Select main option":
            for widget in self.image_frame.winfo_children():
                widget.destroy()
                
            self.image_label = ttk.Label(self.image_frame)
            self.image_label.pack(expand=True)
            
            self.loaded_images = {
                'image1': {'photo': None, 'path': None},
                'image2': {'photo': None, 'path': None}
            }
            
            self.sub_selection_label.pack(fill="x", padx=5, pady=5)
            self.sub_dropdown.config(values=self.sub_options[selected])
            self.sub_dropdown.pack(fill="x", padx=5, pady=5)
            self.sub_dropdown.set("Select sub-option")
            self.selected_sub_option.trace('w', self.show_load_button)
            add_log(self.log_text, f"Main option selected: {selected}")
        else:
            self.sub_selection_label.pack_forget()
            self.sub_dropdown.pack_forget()
            self.threshold_frame.pack_forget()
            self.brightness_frame_addition_subtraction.pack_forget()
            self.brightness_frame_multiplication_division.pack_forget()
            self.angle_frame.pack_forget()
            self.flip_frame.pack_forget()
            self.zoom_frame.pack_forget()
            self.translation_frame.pack_forget()
            self.global_threshold_frame.pack_forget()
            self.multi_level_frame.pack_forget()
            self.load_button1.pack_forget()
            self.load_button2.pack_forget()
            self.submit_button.pack_forget()

    def show_load_button(self, *args):
        self.threshold_frame.pack_forget()
        self.brightness_frame_addition_subtraction.pack_forget()
        self.brightness_frame_multiplication_division.pack_forget()
        self.angle_frame.pack_forget()
        self.flip_frame.pack_forget()
        self.zoom_frame.pack_forget()
        self.translation_frame.pack_forget()
        self.global_threshold_frame.pack_forget()
        self.multi_level_frame.pack_forget()
        self.load_button1.pack_forget()
        self.load_button2.pack_forget()
        self.submit_button.pack_forget()
        
        if self.selected_sub_option.get() != "Select sub-option":
            if self.selected_sub_option.get() == "Negative Image":
                self.threshold_frame.pack(fill="x", padx=5, pady=5)
                self.threshold_label.pack(side="left", padx=(0, 5))
                self.threshold_entry.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Brightening Image":
                self.brightness_frame_addition_subtraction.pack(fill="x", padx=5, pady=5)
                self.brightness_label_addition_subtraction.pack(side="left", padx=(0, 5))
                self.brightness_entry_addition_subtraction.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Scalar Addition Image" or self.selected_sub_option.get() == "Scalar Subtraction Image":
                self.brightness_frame_addition_subtraction.pack(fill="x", padx=5, pady=5)
                self.brightness_label_addition_subtraction.pack(side="left", padx=(0, 5))
                self.brightness_entry_addition_subtraction.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Scalar Multiplication Image" or self.selected_sub_option.get() == "Scalar Division Image":
                self.brightness_frame_multiplication_division.pack(fill="x", padx=5, pady=5)
                self.brightness_label_multiplication_division.pack(side="left", padx=(0, 5))
                self.brightness_entry_multiplication_division.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Rotation Image":
                self.angle_frame.pack(fill="x", padx=5, pady=5)
                self.angle_label.pack(side="left", padx=(0, 5))
                self.angle_entry.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Flipping Image":
                self.flip_frame.pack(fill="x", padx=5, pady=5)
                self.flip_label.pack(side="left", padx=(0, 5))
                self.flip_entry.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Zooming Image":
                self.zoom_frame.pack(fill="x", padx=5, pady=5)
                self.zoom_label.pack(side="left", padx=(0, 5))
                self.zoom_entry.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Translation Image":
                self.translation_frame.pack(fill="x", padx=5, pady=5)
                self.shift_x_label.pack(side="left", padx=(0, 5))
                self.shift_x_entry.pack(side="left", fill="x", expand=True)
                self.shift_y_label.pack(side="left", padx=(0, 5))
                self.shift_y_entry.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Global Thresholding":
                self.global_threshold_frame.pack(fill="x", padx=5, pady=5)
                self.global_threshold_label.pack(side="left", padx=(0, 5))
                self.global_threshold_entry.pack(side="left", fill="x", expand=True)
            elif self.selected_sub_option.get() == "Multi-Level Thresholding":
                self.multi_level_frame.pack(fill="x", padx=5, pady=5)
                self.multi_level_label.pack(side="left", padx=(0, 5))
                self.multi_level_entry.pack(side="left", fill="x", expand=True)
            
            if self.selected_main_option.get() == "Arithmetic Operation":
                if self.selected_sub_option.get() in ["Addition Image", "Subtraction Image", "Multiplication Image"]:
                    self.load_button1.configure(text="Load Image 1")
                    self.load_button1.pack(fill="x", padx=5, pady=5)
                    self.load_button2.pack(fill="x", padx=5, pady=5)
                else:
                    self.load_button1.configure(text="Load Image")
                    self.load_button1.pack(fill="x", padx=5, pady=5)
                self.submit_button.pack(fill="x", padx=5, pady=10)
            else:
                self.load_button1.configure(text="Load Image")
                self.load_button1.pack(fill="x", padx=5, pady=5)
                self.submit_button.pack(fill="x", padx=5, pady=10)
                
            add_log(self.log_text, f"Sub option selected: {self.selected_sub_option.get()}")

    def calculate_histogram(self, image):
        if len(image.shape) == 3:
            hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
            hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
            hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])
            return hist_r, hist_g, hist_b
        else:
            hist = cv2.calcHist([image], [0], None, [256], [0, 256])
            return hist

    def show_histogram(self, image):
        plt.figure(figsize=(8, 6))
        if len(image.shape) == 3:
            hist_r, hist_g, hist_b = self.calculate_histogram(image)
            plt.plot(hist_r, color='red', label='Red')
            plt.plot(hist_g, color='green', label='Green')
            plt.plot(hist_b, color='blue', label='Blue')
            plt.legend()
        else:
            hist = self.calculate_histogram(image)
            plt.plot(hist, color='gray')
        
        plt.title('Image Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def equalize_histogram(self, image):
        if len(image.shape) == 3:
            img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
            return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        else:
            return cv2.equalizeHist(image)

    def normalize_histogram(self, image):
        return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    def stretch_histogram(self, image):
        if len(image.shape) == 3:
            b, g, r = cv2.split(image)
            b_stretched = cv2.normalize(b, None, 0, 255, cv2.NORM_MINMAX)
            g_stretched = cv2.normalize(g, None, 0, 255, cv2.NORM_MINMAX)
            r_stretched = cv2.normalize(r, None, 0, 255, cv2.NORM_MINMAX)
            return cv2.merge((b_stretched, g_stretched, r_stretched))
        else:
            return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    def show_histogram_in_gui(self, histogram, title="Histogram"):
        display_frame = ttk.Frame(self.image_frame)
        display_frame.pack(fill="both", expand=True)
        
        image_frame = ttk.Frame(display_frame)
        image_frame.pack(side='left', fill='both', expand=True)
        
        hist_frame = ttk.Frame(display_frame)
        hist_frame.pack(side='right', fill='both', expand=True)
        
        if hasattr(self, 'current_image_photo'):
            image_label = ttk.Label(image_frame, image=self.current_image_photo)
            image_label.pack(fill='both', expand=True)
        
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=hist_frame)
        canvas.draw()
        
        ax = fig.add_subplot(111)
        ax.bar(range(len(histogram)), histogram)
        ax.set_title(title)
        ax.set_xlabel('Pixel Value')
        ax.set_ylabel('Frequency')
        
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def handle_selection(self):
        main_choice = self.selected_main_option.get()
        sub_choice = self.selected_sub_option.get()
        
        try:
            window_width = self.root.winfo_width() - 100
            
            def resize_if_needed(img):
                height, width = img.shape[:2]
                if width > window_width:
                    aspect_ratio = height / width
                    new_width = window_width
                    new_height = int(new_width * aspect_ratio)
                    resized_img = cv2.resize(img, (new_width, new_height))
                    
                    add_log(self.log_text, f"Image resized from {width}x{height} to {new_width}x{new_height} pixels")
                    add_log(self.log_text, "Reason: Image width exceeded window width, resized to fit window while maintaining aspect ratio")
                    
                    return resized_img
                return img
            
            if main_choice == "Arithmetic Operation":
                if sub_choice in ["Addition Image", "Subtraction Image", "Multiplication Image"]:
                    if not all(self.loaded_images[key]['path'] for key in ['image1', 'image2']):
                        add_log(self.log_text, "Please load both images first")
                        return
                
                if sub_choice == "Addition Image":
                    processed_img = self.arithmetic_service.process_addition_image(
                        self.loaded_images['image1']['path'],
                        self.loaded_images['image2']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied addition operation")
                elif sub_choice == "Subtraction Image":
                    processed_img = self.arithmetic_service.process_subtraction_image(
                        self.loaded_images['image1']['path'],
                        self.loaded_images['image2']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied subtraction operation")
                elif sub_choice == "Multiplication Image":
                    processed_img = self.arithmetic_service.process_multiplication_image(
                        self.loaded_images['image1']['path'],
                        self.loaded_images['image2']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied multiplication operation")
                elif sub_choice == "Scalar Addition Image":
                    try:
                        brightness = int(self.brightness_entry_addition_subtraction.get())
                        if brightness < 0 or brightness > 255:
                            raise ValueError("Brightness must be between 0 and 255")
                        processed_img = self.arithmetic_service.process_scalar_addition_image(self.loaded_images['image1']['path'], brightness)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied scalar addition with value: {brightness}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid brightness value: {ve}")
                elif sub_choice == "Scalar Subtraction Image":
                    try:
                        brightness = int(self.brightness_entry_addition_subtraction.get())
                        if brightness < 0 or brightness > 255:
                            raise ValueError("Brightness must be between 0 and 255")
                        processed_img = self.arithmetic_service.process_scalar_subtraction_image(self.loaded_images['image1']['path'], brightness)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied scalar subtraction with value: {brightness}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid brightness value: {ve}")
                elif sub_choice == "Scalar Multiplication Image":
                    try:
                        brightness = float(self.brightness_entry_multiplication_division.get())
                        if brightness < 0 or brightness > 25:
                            raise ValueError("Brightness must be between 0 and 25")
                        processed_img = self.arithmetic_service.process_scalar_multiplication_image(self.loaded_images['image1']['path'], brightness)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied scalar multiplication with value: {brightness}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid brightness value: {ve}")
                elif sub_choice == "Scalar Division Image":
                    try:
                        brightness = float(self.brightness_entry_multiplication_division.get())
                        if brightness < 0 or brightness > 25:
                            raise ValueError("Brightness must be between 0 and 25")
                        processed_img = self.arithmetic_service.process_scalar_division_image(self.loaded_images['image1']['path'], brightness)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied scalar division with value: {brightness}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid brightness value: {ve}")
            elif main_choice == "General Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return
                    
                if sub_choice == "Negative Image":
                    try:
                        threshold = int(self.threshold_entry.get())
                        if threshold < 0 or threshold > 255:
                            raise ValueError("Threshold must be between 0 and 255")
                        processed_img = self.general_service.process_negative_image(self.loaded_images['image1']['path'], threshold)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied negative image effect with threshold: {threshold}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid threshold value: {ve}")
                elif sub_choice == "Grayscale Image":
                    processed_img = self.general_service.process_grayscale_image(self.loaded_images['image1']['path'])
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied grayscale effect")
                elif sub_choice == "Brightening Image":
                    try:
                        brightness = int(self.brightness_entry_addition_subtraction.get())
                        if brightness < 0 or brightness > 255:
                            raise ValueError("Brightness must be between 0 and 255")
                        processed_img = self.general_service.process_brightening(self.loaded_images['image1']['path'], brightness)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied brightening effect with value: {brightness}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid brightness value: {ve}")
            elif main_choice == "Geometry Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return

                if sub_choice == "Flipping Image":
                    try:
                        flip_code = int(self.flip_entry.get())
                        if flip_code not in [-1, 0, 1]:
                            raise ValueError("Flip code must be -1, 0, or 1")
                        processed_img = self.geometry_service.process_flipping_image(self.loaded_images['image1']['path'], flip_code)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied flipping with code: {flip_code}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid flip code: {ve}")
                elif sub_choice == "Rotation Image":
                    try:
                        angle = float(self.angle_entry.get())
                        if angle < 0 or angle > 360:
                            raise ValueError("Angle must be between 0 and 360")
                        processed_img = self.geometry_service.process_rotation_image(self.loaded_images['image1']['path'], angle)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied rotation with angle: {angle}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid angle value: {ve}")
                elif sub_choice == "Translation Image":
                    try:
                        shift_x = int(self.shift_x_entry.get())
                        shift_y = int(self.shift_y_entry.get())
                        processed_img = self.geometry_service.process_translation_image(self.loaded_images['image1']['path'], shift_x, shift_y)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied translation with shift X: {shift_x}, shift Y: {shift_y}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid shift values: {ve}")
                elif sub_choice == "Zooming Image":
                    try:
                        zoom_factor = float(self.zoom_entry.get())
                        if zoom_factor < 0 or zoom_factor > 3:
                            raise ValueError("Zoom factor must be between 0 and 3")
                        processed_img = self.geometry_service.process_zooming_image(self.loaded_images['image1']['path'], zoom_factor)
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied zooming with factor: {zoom_factor}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid zoom factor: {ve}")
                else:
                    self.image_label.configure(image=self.loaded_images['image1']['photo'])
                    self.image_label.image = self.loaded_images['image1']['photo']
                    add_log(self.log_text, "Showing original image")
            elif main_choice == "Histogram Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return
                
                for widget in self.image_frame.winfo_children():
                    widget.destroy()
                
                display_frame = ttk.Frame(self.image_frame)
                display_frame.pack(fill="both", expand=True)
                
                hist_frame = ttk.Frame(display_frame)
                hist_frame.pack(side='top', fill='both', expand=True)
                
                image_frame = ttk.Frame(display_frame)
                image_frame.pack(side='bottom', fill='both', expand=True)
                
                if sub_choice == "Equalization":
                    processed_img, histogram = self.histogram_service.process_equalization_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    
                    fig = plt.Figure(figsize=(6, 4), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=hist_frame)
                    canvas.draw()
                    
                    ax = fig.add_subplot(111)
                    ax.bar(range(len(histogram)), histogram.ravel())
                    ax.set_title('Equalized Histogram')
                    ax.set_xlabel('Pixel Value')
                    ax.set_ylabel('Frequency')
                    
                    canvas.get_tk_widget().pack(fill='both', expand=True)
                    
                    processed_img_rgb = cv2.cvtColor(processed_img.astype(np.uint8), cv2.COLOR_GRAY2RGB)
                    pil_img = Image.fromarray(processed_img_rgb)
                    photo = ImageTk.PhotoImage(pil_img)
                    img_label = ttk.Label(image_frame, image=photo)
                    img_label.image = photo
                    img_label.pack(expand=True)
                    add_log(self.log_text, "Applied equalization")

                elif sub_choice == "Normalization":
                    processed_img, histogram = self.histogram_service.process_normalization_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    
                    fig = plt.Figure(figsize=(6, 4), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=hist_frame)
                    canvas.draw()
                    
                    ax = fig.add_subplot(111)
                    ax.bar(range(len(histogram)), histogram.ravel())
                    ax.set_title('Normalized Histogram')
                    ax.set_xlabel('Pixel Value')
                    ax.set_ylabel('Frequency')
                    
                    canvas.get_tk_widget().pack(fill='both', expand=True)
                    
                    processed_img_rgb = cv2.cvtColor(processed_img.astype(np.uint8), cv2.COLOR_GRAY2RGB)
                    pil_img = Image.fromarray(processed_img_rgb)
                    photo = ImageTk.PhotoImage(pil_img)
                    img_label = ttk.Label(image_frame, image=photo)
                    img_label.image = photo
                    img_label.pack(expand=True)
                    add_log(self.log_text, "Applied normalization")
                    
                elif sub_choice == "Stretching":
                    processed_img, histogram = self.histogram_service.process_stretching_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    
                    fig = plt.Figure(figsize=(6, 4), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=hist_frame)
                    canvas.draw()
                    
                    ax = fig.add_subplot(111)
                    ax.bar(range(len(histogram)), histogram.ravel())
                    ax.set_title('Stretched Histogram')
                    ax.set_xlabel('Pixel Value')
                    ax.set_ylabel('Frequency')
                    
                    canvas.get_tk_widget().pack(fill='both', expand=True)
                    
                    processed_img_rgb = cv2.cvtColor(processed_img.astype(np.uint8), cv2.COLOR_GRAY2RGB)
                    pil_img = Image.fromarray(processed_img_rgb)
                    photo = ImageTk.PhotoImage(pil_img)
                    img_label = ttk.Label(image_frame, image=photo)
                    img_label.image = photo
                    img_label.pack(expand=True)
                    add_log(self.log_text, "Applied stretching")
            elif main_choice == "Filtering Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return
                
                if sub_choice == "Edge Detection":
                    processed_img = self.filtering_service.process_edge_detection_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied edge detection filter")
                    
                elif sub_choice == "Highpass":
                    processed_img = self.filtering_service.process_highpass_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied highpass filter")
                    
                elif sub_choice == "Lowpass":
                    processed_img = self.filtering_service.process_lowpass_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied lowpass filter")
                    
                elif sub_choice == "Mean":
                    processed_img = self.filtering_service.process_mean_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied mean filter")
                    
                elif sub_choice == "Median":
                    processed_img = self.filtering_service.process_median_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied median filter")
            elif main_choice == "Morphology Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return

                for widget in self.image_frame.winfo_children():
                    widget.destroy()

                display_frame = ttk.Frame(self.image_frame)
                display_frame.pack(fill="both", expand=True)

                if sub_choice == "Opening":
                    eroded_img, dilated_img = self.morphology_service.process_opening_image(
                        self.loaded_images['image1']['path']
                    )
                    
                    original_img = cv2.cvtColor(cv2.imread(self.loaded_images['image1']['path']), cv2.COLOR_BGR2RGB)
                    original_img = resize_if_needed(original_img)
                    images = [
                        ("Original", original_img),
                        ("Eroded", eroded_img),
                        ("Opened", dilated_img)
                    ]
                    
                    for title, img in images:
                        frame = ttk.Frame(display_frame)
                        frame.pack(side="top", fill="both", expand=True, pady=5)
                        
                        label = ttk.Label(frame, text=title)
                        label.pack()
                        
                        pil_img = Image.fromarray(img)
                        photo = ImageTk.PhotoImage(pil_img)
                        img_label = ttk.Label(frame, image=photo)
                        img_label.image = photo
                        img_label.pack(expand=True)
                    
                    add_log(self.log_text, "Applied opening morphology")

                elif sub_choice == "Closing":
                    closed_img = self.morphology_service.process_closing_image(
                        self.loaded_images['image1']['path']
                    )
                    
                    images = [
                        ("Original", cv2.cvtColor(cv2.imread(self.loaded_images['image1']['path']), cv2.COLOR_BGR2RGB)),
                        ("Closed", closed_img)
                    ]
                    
                    for title, img in images:
                        frame = ttk.Frame(display_frame)
                        frame.pack(side="top", fill="both", expand=True, pady=5)
                        
                        label = ttk.Label(frame, text=title)
                        label.pack()
                        
                        pil_img = Image.fromarray(img)
                        photo = ImageTk.PhotoImage(pil_img)
                        img_label = ttk.Label(frame, image=photo)
                        img_label.image = photo
                        img_label.pack(expand=True)
                    
                    add_log(self.log_text, "Applied closing morphology")

                elif sub_choice == "Erosion":
                    eroded_4x4, eroded_6x6 = self.morphology_service.process_erosion_image(
                        self.loaded_images['image1']['path']
                    )
                    
                    images = [
                        ("Original", cv2.cvtColor(cv2.imread(self.loaded_images['image1']['path']), cv2.COLOR_BGR2RGB)),
                        ("4x4 Kernel", eroded_4x4),
                        ("6x6 Kernel", eroded_6x6)
                    ]
                    
                    for title, img in images:
                        frame = ttk.Frame(display_frame)
                        frame.pack(side="top", fill="both", expand=True, pady=5)
                        
                        label = ttk.Label(frame, text=title)
                        label.pack()
                        
                        pil_img = Image.fromarray(img)
                        photo = ImageTk.PhotoImage(pil_img)
                        img_label = ttk.Label(frame, image=photo)
                        img_label.image = photo
                        img_label.pack(expand=True)
                    
                    add_log(self.log_text, "Applied erosion morphology")

                elif sub_choice == "Dilation":
                    dilated_4x4, dilated_7x7 = self.morphology_service.process_dilation_image(
                        self.loaded_images['image1']['path']
                    )
                    
                    images = [
                        ("Original", cv2.cvtColor(cv2.imread(self.loaded_images['image1']['path']), cv2.COLOR_BGR2RGB)),
                        ("4x4 Kernel", dilated_4x4),
                        ("7x7 Kernel", dilated_7x7)
                    ]
                    
                    for title, img in images:
                        frame = ttk.Frame(display_frame)
                        frame.pack(side="top", fill="both", expand=True, pady=5)
                        
                        label = ttk.Label(frame, text=title)
                        label.pack()
                        
                        pil_img = Image.fromarray(img)
                        photo = ImageTk.PhotoImage(pil_img)
                        img_label = ttk.Label(frame, image=photo)
                        img_label.image = photo
                        img_label.pack(expand=True)
                    
                    add_log(self.log_text, "Applied dilation morphology")
            elif main_choice == "Edge Detection Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return
                
                if sub_choice == "Canny Edge Detection":
                    processed_img = self.edge_detection_service.process_canny_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied canny edge detection")
                
                elif sub_choice == "Frei-Chen Edge Detection":
                    processed_img = self.edge_detection_service.process_freichen_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Frei-Chen edge detection")

                elif sub_choice == "Gradient Edge Detection":
                    processed_img = self.edge_detection_service.process_gradient_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied gradient edge detection")

                elif sub_choice == "Laplacian Edge Detection":
                    processed_img = self.edge_detection_service.process_laplacian_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Laplacian edge detection")

                elif sub_choice == "Laplacian of Gaussian Edge Detection":
                    processed_img = self.edge_detection_service.process_log_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied LOG edge detection")

                elif sub_choice == "Prewitt Edge Detection":
                    processed_img = self.edge_detection_service.process_prewitt_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Prewitt edge detection")

                elif sub_choice == "Roberts Edge Detection":
                    processed_img = self.edge_detection_service.process_roberts_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Roberts edge detection")

                elif sub_choice == "Sobel Edge Detection":
                    processed_img = self.edge_detection_service.process_sobel_image(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Sobel edge detection")
            elif main_choice == "Thresholding Operation":
                if not self.loaded_images['image1']['path']:
                    add_log(self.log_text, "Please load an image first")
                    return
                
                if sub_choice == "Otsu Thresholding":
                    processed_img = self.thresholding_service.process_otsu_thresholding(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Otsu thresholding")

                elif sub_choice == "Multi-Level Thresholding":
                    try:
                        levels = int(self.multi_level_entry.get())
                        if levels < 2 or levels > 4:
                            raise ValueError("Number of levels must be between 2 and 4")
                        processed_img = self.thresholding_service.process_multi_level_thresholding(
                            self.loaded_images['image1']['path'],
                            levels
                        )
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied Multi-Level thresholding with {levels} levels")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid levels value: {ve}")

                elif sub_choice == "Global Thresholding":
                    try:
                        threshold = int(self.global_threshold_entry.get())
                        if threshold < 0 or threshold > 255:
                            raise ValueError("Threshold must be between 0 and 255")
                        processed_img = self.thresholding_service.process_global_thresholding(
                            self.loaded_images['image1']['path'],
                            threshold
                        )
                        processed_img = resize_if_needed(processed_img)
                        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(processed_img)
                        photo = ImageTk.PhotoImage(pil_img)
                        self.image_label.configure(image=photo)
                        self.image_label.image = photo
                        add_log(self.log_text, f"Applied Global thresholding with threshold: {threshold}")
                    except ValueError as ve:
                        add_log(self.log_text, f"Invalid threshold value: {ve}")

                elif sub_choice == "Adaptive Thresholding":
                    processed_img = self.thresholding_service.process_adaptive_thresholding(
                        self.loaded_images['image1']['path']
                    )
                    processed_img = resize_if_needed(processed_img)
                    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(processed_img)
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.configure(image=photo)
                    self.image_label.image = photo
                    add_log(self.log_text, "Applied Adaptive thresholding")

            self.root.update_idletasks()
        except Exception as e:
            add_log(self.log_text, f"Error displaying image: {e}")

    def run(self):
        self.root.mainloop()
