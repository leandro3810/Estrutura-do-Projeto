#!/bin/bash
python -m venv flask-env
source flask-env/bin/activate  # Para Linux/Mac
# No Windows: flask-env\Scripts\activate
pip install Flask
