import logging
import time

from commons.commons import decode_base64_img
from flask import Blueprint, request

from flask_app.model import model_store

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/predict', methods=['POST'])
def predict():
    logging.info("POST /predict")
    req = request.get_json()

    if 'img' not in req:
        logging.error('img params missing in request')
        return {'error': 'img params missing in request'}, 205

    try:
        start_time = time.time()

        input_image = decode_base64_img(req['img'])
        prediction = model_store['faster_rcnn'].predict(input_image)

        if req.get('response_type', 'raw') == 'raw':
            response = model_store['faster_rcnn'].format_prediction(prediction)
        # else:
        #     return model_store['faster_rcnn'].get_visualization(input_image, prediction)

        end_time = time.time()
        logging.info('Total prediction time: %.3fs.' % (end_time - start_time))

        return response
    except Exception as error:
        logging.exception(error)
        return {'error': 'Error in prediction'}
