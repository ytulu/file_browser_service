# src/__init__.py


from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)

@api.route('/hello')
@api.doc(params={'id': 'hello world'})
class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world'})

api.add_resource(HelloWorld, '/hello')