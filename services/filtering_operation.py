from utils.index import validate_image
from repositories.filtering_operation import (
    edge_detection,
    highpass,
    lowpass,
    mean,
    median,
)

class FilteringOperationService:
    def __init__(self):
        pass
        
    def process_edge_detection_image(self, image_path):
        img = validate_image(image_path)
        edge_detection_processor = edge_detection.EdgeDetectionFilter(img)
        edge_detection_img = edge_detection_processor.process()
        return edge_detection_img

    def process_highpass_image(self, image_path):
        img = validate_image(image_path)
        highpass_processor = highpass.HighpassFilter(img)
        highpass_img = highpass_processor.process()
        return highpass_img

    def process_lowpass_image(self, image_path):
        img = validate_image(image_path)
        lowpass_processor = lowpass.LowpassFilter(img)
        lowpass_img = lowpass_processor.process()
        return lowpass_img

    def process_mean_image(self, image_path):
        img = validate_image(image_path)
        mean_processor = mean.MeanFilter(img)
        mean_img = mean_processor.process()
        return mean_img

    def process_median_image(self, image_path):
        img = validate_image(image_path)
        median_processor = median.MedianFilter(img)
        median_img = median_processor.process()
        return median_img
