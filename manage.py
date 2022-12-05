import os
from flask.cli import FlaskGroup

from src import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    app.config['UPLOAD_PATH'] = os.environ.get('UPLOAD_PATH')
    cli()
