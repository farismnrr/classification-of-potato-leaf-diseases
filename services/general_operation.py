from utils.index import validate_image
from repositories.general_operation import (
    brightening,
    negative, 
    grayscale, 
)

class GeneralOperationService:
    def __init__(self):
        pass
        
    def process_negative_image(self, image_path, threshold):
        img = validate_image(image_path)
        negative_processor = negative.NegativeOperation(img, threshold)
        negative_img = negative_processor.process()
        return negative_img

    def process_grayscale_image(self, image_path):
        img = validate_image(image_path)
        grayscale_processor = grayscale.GrayscaleOperation(img)
        grayscale_img = grayscale_processor.process()
        return grayscale_img

    def process_brightening(self, image_path, brightness_factor):
        img = validate_image(image_path)
        brightening_img = brightening.BrighteningOperation(img, brightness_factor)
        brightening_img = brightening_img.process()
        return brightening_img