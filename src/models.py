import os
from flask import send_from_directory, jsonify

ALLOWED_EXTENSIONS = set(['txt', 'json'])
UPLOAD_FOLDER = 'uploads'
class fileModel:
    def __init__(self, filename, owner, size, permissions):
        self.filename = filename
        self.owner = owner
        self.size = size
        self.permissions = permissions

    """
    Determine if the file is allowed in upload directory
    """
    def allowed_file(self, filename):
        print (filename) # debug print
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    """
    Get the file atrributes and return a json object
    """
    def get_file(self, filename):
        head, tail = os.path.split(filename)
        file_object = {
            'name': str(tail),
            'owner': os.stat(filename).st_uid,
            'size': os.stat(filename).st_size,
            'permissions': os.stat(filename).st_mode,
        }
        return file_object

    """
    Search the upload directory for files and directories
    """
    def get_files(self, filename):
        for root, directories, files in os.os.walk(UPLOAD_FOLDER):
            # return the file contents
            if filename in files:
                print (self.get_file_attributes(os.path.join(root, filename))) # debug print
                response = send_from_directory(root, filename)
                response.status_code = 200
                return response

            # if dir return json of dir contents
            elif filename in directories:
                files_col = []
                for file in files:
                    files_col.append(self.get_file_attributes(os.path.join(root, file)))
                response = jsonify({'data' : files_col, "Directories" : directories})
                response.status_code = 200
                return response
        # handle file not found
        response = jsonify({'data' : 'No directory(s) or file(s) found for ' + filename})
        response.status_code = 404
        return response