from utils.index import validate_image
from repositories.arithmetic_operation import (
    addition,
    subtraction,
    multiplication,
    scalar_addition,
    scalar_subtraction,
    scalar_multiplication,
    scalar_division,
)

class ArithmeticOperationService:
    def __init__(self):
        pass
        
    def process_addition_image(self, image_path1, image_path2):
        img1 = validate_image(image_path1)
        img2 = validate_image(image_path2)
        addition_processor = addition.AdditionArithmetic(img1, img2)
        addition_img = addition_processor.process()
        return addition_img

    def process_subtraction_image(self, image_path1, image_path2):
        img1 = validate_image(image_path1)
        img2 = validate_image(image_path2)
        subtraction_processor = subtraction.SubtractionArithmetic(img1, img2)
        subtraction_img = subtraction_processor.process()
        return subtraction_img

    def process_multiplication_image(self, image_path1, image_path2):
        img1 = validate_image(image_path1)
        img2 = validate_image(image_path2)
        multiplication_processor = multiplication.MultiplicationArithmetic(img1, img2)
        multiplication_img = multiplication_processor.process()
        return multiplication_img

    def process_scalar_addition_image(self, image_path, brightness_factor):
        img = validate_image(image_path)
        scalar_addition_processor = scalar_addition.ScalarAdditionArithmetic(img, brightness_factor)
        scalar_addition_img = scalar_addition_processor.process()
        return scalar_addition_img

    def process_scalar_subtraction_image(self, image_path, brightness_factor):
        img = validate_image(image_path)
        scalar_subtraction_processor = scalar_subtraction.ScalarSubtractionArithmetic(img, brightness_factor)
        scalar_subtraction_img = scalar_subtraction_processor.process()
        return scalar_subtraction_img

    def process_scalar_multiplication_image(self, image_path, brightness_factor):
        img = validate_image(image_path)
        scalar_multiplication_processor = scalar_multiplication.ScalarMultiplicationArithmetic(img, brightness_factor)
        scalar_multiplication_img = scalar_multiplication_processor.process()
        return scalar_multiplication_img

    def process_scalar_division_image(self, image_path, brightness_factor):
        img = validate_image(image_path)
        scalar_division_processor = scalar_division.ScalarDivisionArithmetic(img, brightness_factor)
        scalar_division_img = scalar_division_processor.process()
        return scalar_division_img