import os
import sys

from flask import Flask, jsonify, send_from_directory
from flask_restx import Api, Resource

from src.utils import allowed_file, get_file, get_file_attr

UPLOAD_PATH = os.environ.get("UPLOAD_PATH")

app = Flask(__name__)

api = Api(app)

# set config (will be used for upload directory injection)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)
# print(app.config, file=sys.stderr)


@api.route("/api/")
@api.doc(params={"/": "<path:path>"})
class FileRootPath(Resource):
    """endpoint to get file or directory contents of the root directory"""

    """return the file path, if direectory,
    return json of files and other directories"""

    def output(self, path):
        """return the file path, if direectory,
        return json of files and other directories"""
        if os.path.isdir(path):
            for root, directories, files in os.walk(path):
                files_col = []
                for file in files:
                    filepath = os.path.join(root, file)
                    files_col.append(get_file_attr(filepath))
                return jsonify({"data": files_col, "Dirs": directories})
            # return jsonify({"files": os.listdir(path)})
        elif os.path.isfile(path):
            if allowed_file(path):
                return get_file(path)
        else:
            return jsonify({"data": "No file(s) found for " + path})

    def get(self):
        """return the file path, if direectory,
        return json of files and other directories"""
        path = "src/uploads"
        return self.output(path)


api.add_resource(FileRootPath, "/api/")


@api.route("/api/<path:path>", methods=["GET"])
@api.doc(params={"/": "<path:path>"})
class FilePath(Resource):
    """endpoint to get file or directory contents"""

    from src.utils import allowed_file, get_file, get_file_attr

    """return the file path, if direectory,
    return json of files and other directories"""

    def output(self, path):
        """return the file path, if direectory,
        return json of files and other directories"""

        if os.path.isfile(os.path.join(UPLOAD_PATH, path)):
            response = send_from_directory(UPLOAD_PATH, path)
            response.status_code = 200
            # debug print
            attr = get_file_attr(os.path.join(UPLOAD_PATH, path))
            print(attr, file=sys.stderr)
            return response

        elif os.path.isdir(os.path.join(UPLOAD_PATH, path)):
            files = []
            dirs = []
            for stuff in os.listdir(os.path.join(UPLOAD_PATH, path)):
                if os.path.isfile(os.path.join(UPLOAD_PATH, path, stuff)):
                    fl = os.path.join(UPLOAD_PATH, path, stuff)
                    files_col = get_file_attr(fl)
                    files.append(files_col)

                elif os.path.isdir(os.path.join(UPLOAD_PATH, stuff)):
                    dirs.append(stuff)
                    resp = jsonify({"data": {"files": files, "Dirs": dirs}})
                    resp.status_code = 200
                    return response
        else:
            return get_file(path)

    def get(self, path):
        """return the file path, if direectory,
        return json of files and other directories"""
        return self.output(path)


api.add_resource(FilePath, "/api/<path:path>")
