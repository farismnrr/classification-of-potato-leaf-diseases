from utils.index import validate_image
from repositories.thresholding_operation import (
    adaptive,
    otsu,
    globals,
    multi_level,
)

class ThresholdingOperationService:
    def __init__(self):
        pass
        
    def process_adaptive_thresholding(self, image_path, block_size=11, c=2):
        img = validate_image(image_path)
        adaptive_processor = adaptive.AdaptiveThresholding(img, block_size, c)
        adaptive_img = adaptive_processor.process()
        return adaptive_img
        

    def process_global_thresholding(self, image_path, threshold):
        img = validate_image(image_path)
        global_processor = globals.GlobalsThresholding(img, threshold)
        global_img = global_processor.process()
        return global_img

    def process_otsu_thresholding(self, image_path):
        img = validate_image(image_path)
        otsu_processor = otsu.OtsuThresholding(img)
        otsu_img = otsu_processor.process()
        return otsu_img

    def process_multi_level_thresholding(self, image_path, levels):
        img = validate_image(image_path)
        multi_level_processor = multi_level.MultiLevelThresholding(img, levels)
        multi_level_img = multi_level_processor.process()
        return multi_level_img
