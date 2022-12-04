import os
import sys

from flask import Flask, jsonify
from flask_restx import Resource, Api

UPLOAD_PATH = os.environ.get('UPLOAD_PATH')

app = Flask(__name__)

api = Api(app)

#set config (will be used for upload directory injection)
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
print(app.config, file=sys.stderr)

@api.route('/api/')
@api.doc(params={'/': '<path:path>'})
class FilePath(Resource):
    '''return the file path, if direectory, return json of files and other directories'''
    def output(self, path):
        '''return the file path, if direectory, return json of files and other directories'''
        if os.path.isdir(path):
            return jsonify({"files": os.listdir(path)})
        elif os.path.isfile(path):
            return jsonify({"file": path})
    def get(self):
        '''return the file path, if direectory, return json of files and other directories'''
        path = 'src/uploads'
        return self.output(path)

api.add_resource(FilePath, '/api/{path}')
