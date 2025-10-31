#!/bin/bash

# This script sets up the environment and runs the FastAPI application locally.

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Please create one using 'python -m venv venv'."
    exit 1
fi

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Note: The --reload flag enables auto-reload for development purposes.