from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Moneda(Resource):
    def get(self, module):
        return module+"xxxAffff"

    def post(self, module):
        print("ola k ase")
        return "post request "+module

class Prueba(Resource):
    def get(self):
        return "xxx"


api.add_resource(Moneda, '/entablar/guardar/<string:module>')
api.add_resource(Prueba, '/')

app.run(debug=True)