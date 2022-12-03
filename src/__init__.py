import os
import sys

from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)

#set config (will be used for upload directory injection)
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
#print(app.config, file=sys.stderr)

@api.route('/hello')
@api.doc(params={'id': 'hello world!'})
class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world'})

api.add_resource(HelloWorld, '/hello')