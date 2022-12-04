#!/bin/bash
# This script is executed by the first_start.sh script for first time setup

# build the image
echo "Building the image..."
docker-compose build
echo "Done."

# run the container in detached mode
echo "Running the container..."
docker-compose up -d

# run the tests in the container
echo "Running the tests..."
docker-compose exec -T api python -m pytest "src/tests"

# Show the contents of the root uploads folder
echo "Showing the contents of the root uploads folder..."
docker run --network container:file-browser-service appropriate/curl -s --retry 10 --retry-connrefused http://localhost:5000/api/

# Show the swagger docs
echo "Showing the swagger docs..."
open http://localhost:5004

# show the endpoints
open http://localhost:5004/api
