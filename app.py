from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World! Emotioni-Recognition works"}


api.add_resource(HelloWorld, "/helloWorld")


image_post_args = reqparse.RequestParser()
image_post_args.add_argument(
    "name", type=str, help="you didnt send name", required=True)


class UploadImage(Resource):
    def post(self):
        args = image_post_args.parse_args()
        print(args.name)
        return{"data": "post works now 2"}


api.add_resource(UploadImage, "/uploadImage")


if __name__ == "__main__":
    app.run(debug=True)
