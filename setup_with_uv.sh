#!/bin/bash

# This script demonstrates how to set up the project using uv package manager

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Installing uv..."
    pip install uv
fi

echo "Creating virtual environment with uv..."
uv venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies with uv..."
uv pip install -e .

echo "Setup complete! You can now run the crawler with: python crawler.py"
echo "To activate this environment in the future, run: source .venv/bin/activate"