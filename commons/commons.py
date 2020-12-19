import base64

import cv2
import numpy as np


def decode_base64_img(encoded_image: str) -> np.array:
    decoded_image = base64.b64decode(encoded_image)
    nparr = np.frombuffer(decoded_image, dtype=np.uint8)
    # channels format used by OpenCV is BGR order
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def encode_img_to_base_64(image: np.array, ext='.jpeg') -> str:
    _, buffer = cv2.imencode(ext, image)
    return base64.b64encode(buffer).decode("utf-8")
