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

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc/')
app.register_blueprint(blueprint)

@api.route('/')
@api.doc(params={'id': 'hello world!'})
class HelloWorld(Resource):
    '''simple hello world'''
    def get(self):
        '''get hello world'''
        return jsonify({'hello': 'world'})

api.add_resource(HelloWorld, '/hello')
