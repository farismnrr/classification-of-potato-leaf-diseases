from utils.index import validate_image
from repositories.geometry_operation import (
    flipping,
    rotation,
    translation,
    zooming,
)

class GeometryOperationService:
    def __init__(self):
        pass
        
    def process_flipping_image(self, image_path, flip_code):
        img = validate_image(image_path)
        flipping_processor = flipping.FlippingGeometry(img)
        flipped_img = flipping_processor.process(flip_code)
        return flipped_img

    def process_rotation_image(self, image_path, angle):
        img = validate_image(image_path)
        rotation_processor = rotation.RotationGeometry(img)
        rotated_img = rotation_processor.process(angle)
        return rotated_img

    def process_translation_image(self, image_path, shift_x, shift_y):
        img = validate_image(image_path)
        translation_processor = translation.TranslationGeometry(img)
        translated_img = translation_processor.process(shift_x, shift_y)
        return translated_img

    def process_zooming_image(self, image_path, zoom_factor):
        img = validate_image(image_path)
        zooming_processor = zooming.ZoomingGeometry(img)
        zoomed_img = zooming_processor.process(zoom_factor)
        return zoomed_img
