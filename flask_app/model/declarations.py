import logging
from abc import ABC, abstractmethod

from commons.commons import encode_img_to_base_64
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer


class BaseModel(ABC):
    def __init__(self):
        self.predictor = None

    @abstractmethod
    def init_model(self, config):
        pass

    @abstractmethod
    def predict(self, input_image):
        pass

    @abstractmethod
    def format_prediction(self, prediction):
        pass

    @abstractmethod
    def get_visualization(self, input_image, outputs):
        pass


class FasterRCNN(BaseModel):

    def init_model(self, config):
        self.cfg = self.get_config(config)
        self.metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0])
        self.predictor = DefaultPredictor(self.cfg)

    def get_config(self, config):
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file(
            "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
            "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
        cfg.MODEL.RETINANET.SCORE_THRESH_TEST = 0.5
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
        cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = 0.5

        if config.get('CPU'):
            cfg.MODEL.DEVICE = 'cpu'
        return cfg

    def predict(self, input_image):
        if self.predictor is None:
            logging.error('Model not initialized. Call init_model first.')
        return self.predictor(input_image)

    def format_prediction(self, prediction):
        response = {}
        response['instances'] = []

        coordinates = prediction['instances'].pred_boxes.tensor.cpu().numpy()
        pred_classes = prediction['instances'].pred_classes.cpu().numpy()
        scores = prediction['instances'].scores.cpu().numpy()

        for i in range(len(prediction['instances'])):
            instance_result = {
                'x1': str(coordinates[i, 0]),
                'y1': str(coordinates[i, 1]),
                'x2': str(coordinates[i, 2]),
                'y2': str(coordinates[i, 3]),
                'class': self.metadata.thing_classes[pred_classes[i]],
                'score': str(scores[i])
            }
            response['instances'].append(instance_result)

        return response

    def get_visualization(self, input_image, outputs):
        logging.info('Generating visualization...')
        v = Visualizer(input_image[:, :, ::-1], self.metadata)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        encoded_img = encode_img_to_base_64(out.get_image())
        return {'img': encoded_img}
