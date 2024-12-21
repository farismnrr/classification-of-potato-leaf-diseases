from utils.index import validate_image
from repositories.histogram_operation import (
    equalization,
    normalization,
    stretching,
)

class HistogramOperationService:
    def __init__(self):
        pass
        
    def process_equalization_image(self, image_path, k=8):
        img = validate_image(image_path)
        processor = equalization.EqualizationHistogram(img, k)
        processed_img = processor.process()
        histogram = processor.get_histogram()
        return processed_img, histogram

    def process_normalization_image(self, image_path):
        img = validate_image(image_path)
        processor = normalization.NormalizationHistogram(img)
        processed_img = processor.process()
        histogram = processor.get_histogram()
        return processed_img, histogram

    def process_stretching_image(self, image_path):
        img = validate_image(image_path)
        processor = stretching.StretchingHistogram(img)
        processed_img = processor.process()
        histogram = processor.get_histogram()
        return processed_img, histogram
