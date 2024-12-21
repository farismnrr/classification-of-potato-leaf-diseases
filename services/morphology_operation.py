from utils.index import validate_image
from repositories.morphology_operation import (
    closing,
    dilation,
    erosion,
    erosion_edge,
    opening,
)

class MorphologyOperationService:
    def __init__(self):
        pass
        
    def process_closing_image(self, image_path):
        img = validate_image(image_path)
        closing_processor = closing.ClosingMorphology(img)
        closed_img = closing_processor.process()
        return closed_img

    def process_dilation_image(self, image_path):
        img = validate_image(image_path)
        dilation_processor = dilation.DilationMorphology(img)
        dilated_4x4, dilated_7x7 = dilation_processor.process()
        return dilated_4x4, dilated_7x7

    def process_erosion_image(self, image_path):
        img = validate_image(image_path)
        erosion_processor = erosion.ErosionMorphology(img)
        eroded_4x4, eroded_6x6 = erosion_processor.process()
        return eroded_4x4, eroded_6x6

    def process_erosion_edge_image(self, image_path):
        img = validate_image(image_path)
        erosion_edge_processor = erosion_edge.ErosionEdgeMorphology(img)
        eroded_img, edge_img = erosion_edge_processor.process()
        return eroded_img, edge_img

    def process_opening_image(self, image_path):
        img = validate_image(image_path)
        opening_processor = opening.OpeningMorphology(img)
        eroded_img, dilated_img = opening_processor.process()
        return eroded_img, dilated_img
