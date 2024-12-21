from utils.index import validate_image
from repositories.edge_detection_operation import (
    canny,
    freichen,
    gradient,
    laplacian,
    laplacian_of_gaussian,
    prewitt,
    roberts,
    sobel,
)

class EdgeDetectionOperationService:
    def __init__(self):
        pass
        
    def process_canny_image(self, image_path):
        img = validate_image(image_path)
        detector = canny.CannyEdgeDetector()
        return detector.detect(img)

    def process_freichen_image(self, image_path):
        img = validate_image(image_path)
        detector = freichen.FreiChenEdgeDetector()
        return detector.detect_edges(img)

    def process_gradient_image(self, image_path):
        img = validate_image(image_path)
        detector = gradient.GradientEdgeDetector()
        return detector.detect(img)

    def process_laplacian_image(self, image_path):
        img = validate_image(image_path)
        detector = laplacian.LaplacianEdgeDetector()
        return detector.detect(img)

    def process_log_image(self, image_path):
        img = validate_image(image_path)
        detector = laplacian_of_gaussian.LaplacianOfGaussianEdgeDetection(img)
        return detector.process()

    def process_prewitt_image(self, image_path):
        img = validate_image(image_path)
        detector = prewitt.PrewittEdgeDetection(img)
        return detector.process()

    def process_roberts_image(self, image_path):
        img = validate_image(image_path)
        detector = roberts.RobertsEdgeDetection(img)
        return detector.process()

    def process_sobel_image(self, image_path):
        img = validate_image(image_path)
        detector = sobel.SobelEdgeDetection(img)
        return detector.process()

