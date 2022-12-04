#!/bin/bash
# Show the swagger docs
echo "Showing the swagger docs..."
python3 -m webbrowser http://localhost:5004

# show the endpoints
echo "Showing the endpoints..."
python3 -m webbrowser http://localhost:5004/api