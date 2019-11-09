from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
import traceback
import sys

import json

app = Flask(__name__)
CORS(app,expose_headers=["Content-Disposition", "file_name"])
api = Api(app)


class EntryAPI(Resource):
    def get(self, module_name, class_name, method_name):
        obj_loader = Loader(module_name, class_name, method_name, data=request.args)
        response = send_file(filename_or_fp=obj_loader.response['file'])
        response.headers["file_name"] = obj_loader.response['file_name']
        return response

    def post(self, module_name, class_name, method_name):
        #data = request.json

        data = None

        if request.is_json:
            data = request.json
        else:
            data = {
                "files": request.files,
                "form": request.form
            }

        obj_Loader = Loader(module_name, class_name, method_name, data=data)
        return jsonify(obj_Loader.response)

class Loader:
    def __init__(self, module_name, class_name, method_name, data={}):
        mod =  __import__("controller."+module_name, fromlist=[class_name])
        obj_reference = getattr(mod, class_name)
        self.obj = obj_reference()
        method_to_call = getattr(self.obj, method_name)
        self.response = method_to_call(data)


class ImageLoader(Resource):
    def get(self, image_loader):
        try:
            filename = "./upload/images/" + request.args.get('image')
            return send_file(filename, mimetype='image/jpg')
        except FileNotFoundError:
            return send_file("./defaults/default.png", mimetype='image/jpg')


api.add_resource(EntryAPI, '/entablar/<string:module_name>/<string:class_name>/<string:method_name>')
api.add_resource(ImageLoader, '/entablar/<string:image_loader>/')


app.run(debug=True)