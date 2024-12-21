# main.py
from interfaces.index import ImageProcessingGUI
from services.general_operation import GeneralOperationService
from services.arithmetic_operation import ArithmeticOperationService
from services.geometry_operation import GeometryOperationService
from services.histogram_operation import HistogramOperationService
from services.filtering_operation import FilteringOperationService
from services.morphology_operation import MorphologyOperationService
from services.edge_detection_operation import EdgeDetectionOperationService
from services.thresholding_operation import ThresholdingOperationService

if __name__ == "__main__":
    general_service = GeneralOperationService()
    arithmetic_service = ArithmeticOperationService()
    geometry_service = GeometryOperationService()
    histogram_service = HistogramOperationService()
    filtering_service = FilteringOperationService()
    morphology_service = MorphologyOperationService()
    edge_detection_service = EdgeDetectionOperationService()
    thresholding_service = ThresholdingOperationService()
    app = ImageProcessingGUI(general_service, arithmetic_service, geometry_service, histogram_service, filtering_service, morphology_service, edge_detection_service, thresholding_service)
    app.run()
