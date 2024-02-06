#!/bin/bash

# Create python 3.10 virtual environment
python -m venv .venv

# Activate virtual environment.
. .venv/bin/activate

# Pip install required files
pip install -r ./tools/requirements.txt 