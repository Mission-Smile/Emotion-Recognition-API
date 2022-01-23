from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from fer import FER
import cv2
import base64

app = Flask(__name__)
CORS(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World! Emotioni-Recognition works"}


api.add_resource(HelloWorld, "/helloWorld")


image_post_args = reqparse.RequestParser()
image_post_args.add_argument(
    "encodedImage", type=str, help="you didnt send encoded base64 image", required=True)


class UploadImage(Resource):
    def post(self):
        args = image_post_args.parse_args()
        img_base64 = args.encodedImage
        img_base64_no_metadata = img_base64.split(",")[-1]
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(img_base64_no_metadata))
        img = cv2.imread("imageToSave.png")
        detector = FER(mtcnn=True)
        emotion, score = detector.top_emotion(img)

        return{"emotion": emotion, "score": score}


api.add_resource(UploadImage, "/uploadImage")


if __name__ == "__main__":
    app.run(debug=True)
