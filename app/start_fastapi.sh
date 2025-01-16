#!/bin/bash

# Activate the Python virtual environment
source /var/www/html/backend/venv/bin/activate  # Adjust this path to your virtual environment

# Start the FastAPI application using Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

