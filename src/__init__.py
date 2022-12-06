import os
import sys

from flask import Flask, jsonify, send_from_directory
from flask_restx import Api, Resource
from werkzeug.datastructures import FileStorage

from src.utils import add_upload_file, allowed_file, get_file, get_file_attr

UPLOAD_PATH = "src/uploads"

app = Flask(__name__)

api = Api(app)

# set config (will be used for upload directory injection)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

up_par = api.parser()
up_par.add_argument("file", location="files", type=FileStorage, required=True)
# print(app.config, file=sys.stderr)


@api.route("/api/", methods=["GET", "POST"])
@api.doc(params={"/": "Upload a file"})
class FileRootPath(Resource):
    """endpoint to get file or directory contents of the root directory"""

    """return the file path, if direectory,
    return json of files and other directories"""

    def output(self, path):
        """return the file path, if direectory,
        return json of files and other directories"""
        if os.path.isdir(path):
            print(path, file=sys.stderr)
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
        path = UPLOAD_PATH.rstrip("/")
        return self.output(path)

    @api.expect(up_par)
    def post(self):
        args = up_par.parse_args()
        uploaded_file = args["file"]  # This is FileStorage instance
        url = add_upload_file(uploaded_file)
        return {"url": url}, 201


api.add_resource(FileRootPath, "/api/")


@api.route("/api/<path:path>", methods=["GET"])
@api.doc(params={"/": "<path:path>"})
class FilePath(Resource):
    """endpoint to get file or directory contents"""

    """return the file path, if direectory,
    return json of files and other directories"""

    def get(self, path):
        """return the file path, if direectory,
        return json of files and other directories"""
        print("getting path: " + path, file=sys.stderr)
        print(
            "getting full path: " + UPLOAD_PATH.rstrip("/") + "/" + path,
            file=sys.stderr,
        )
        # get current working directory
        cwd = os.getcwd()
        print("cwd: " + cwd, file=sys.stderr)
        print(
            "trying to get path: " + os.path.join(cwd, UPLOAD_PATH, path),
            file=sys.stderr,
        )
        full_path = os.path.join(cwd, UPLOAD_PATH, path)
        for root, directories, files in os.walk(full_path):
            files_col = []
            for file in files:
                filepath = os.path.join(root, file)
                files_col.append(get_file_attr(filepath))
            return jsonify({"data": files_col, "Dirs": directories})
        if os.path.isfile(os.path.join(cwd, UPLOAD_PATH, path)):
            return send_from_directory(os.path.join(cwd, UPLOAD_PATH), path)
        elif os.path.isdir(os.path.join(cwd, UPLOAD_PATH, path)):
            return FileRootPath().output(os.path.join(cwd, UPLOAD_PATH, path))
        else:
            return jsonify({"data": "No file(s) found for " + path})


api.add_resource(FilePath, "/api/<path:path>")
