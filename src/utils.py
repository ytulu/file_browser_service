import os

from flask import jsonify, send_from_directory

ALLOWED_EXTENSIONS = set(["txt", "json"])
UPLOAD_FOLDER = os.environ.get("UPLOAD_PATH")
"""
Determine if the file is allowed in upload directory
"""


def allowed_file(filename):
    return "." in filename and (
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


"""
Get the file atrributes and return a json object
"""


def get_file_attr(filename):
    head, tail = os.path.split(filename)
    file_object = {
        "name": str(tail),
        "owner": os.stat(filename).st_uid,
        "size": os.stat(filename).st_size,
        "permissions": os.stat(filename).st_mode,
    }
    return file_object


"""
Search the upload directory for files and directories
"""


def get_file(filename):
    for root, directories, files in os.walk(UPLOAD_FOLDER):
        # return the file contents
        if filename in files:
            # debug print
            print(get_file_attr(os.path.join(root, filename)))
            resp = send_from_directory(root, filename)
            resp.status_code = 200
            return resp
            # if dir return json of dir contents
        elif filename in directories:
            files_col = []
            for file in files:
                filepath = os.path.join(root, file)
                files_col.append(get_file_attr(filepath))
                resp = jsonify({"data": files_col, "Directories": directories})
                resp.status_code = 200
            return resp
        # handle file not found
        resp = jsonify({"data": "No file(s) found for " + filename})
        resp.status_code = 404
        return resp
