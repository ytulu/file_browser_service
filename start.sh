#!/bin/bash
# This script is executed by the first_start.sh script for first time setup


# Setup the .env file
echo "Running the container..."
UPLOAD_PATH='src/uploads'
if [ $# -gt 0 ]; then
    UPLOAD_PATH=$1
    echo $1
fi
echo "Using the root path...$UPLOAD_PATH"
echo "UPLOAD_PATH=$UPLOAD_PATH" > .env
echo "UPLOAD_PATH_TEST=src/test/test_files" >> .env
docker-compose up -d --build
echo "Done."

# generate the test coverage report
echo "Showing the test coverage report..."
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src" --cov-report html

# run the tests in the container
echo "Running the tests..."
docker-compose exec -T api python -m pytest "src/tests"

# Show the contents of the root uploads folder
echo "Showing the contents of the root uploads folder..."
docker run --network container:file-browser-service appropriate/curl -s --retry 10 --retry-connrefused http://localhost:5000/api/

# show the test coverage report
echo "Showing the test coverage report..."
python3 -m webbrowser htmlcov/index.html
# Show the swagger docs
echo "Showing the swagger docs..."
python3 -m webbrowser http://localhost:5004

# show the endpoints
echo "Showing the endpoints..."
python3 -m webbrowser http://localhost:5004/api
