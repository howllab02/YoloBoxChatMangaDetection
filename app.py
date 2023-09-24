from flask import Flask, jsonify, request
from static.model import YoloModel
import cv2
import numpy as np

app = Flask(__name__)

weight = "static/Yolo_model.pt"


def to_tensor(image_bytes):
    img_np = np.frombuffer(image_bytes, dtype=np.int8)
    cv_img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    return cv_img


@app.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return 'Welcome Box Chat Detection'


@app.route("/inference", methods=["POST"])
def inference():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        model = YoloModel(weight)
        img = to_tensor(img_bytes)
        result = model.predict(bytes_image=img)
        return jsonify({"bbox": result.tolist()})


if __name__ == '__main__':
    app.run()
