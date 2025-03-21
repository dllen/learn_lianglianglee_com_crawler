@echo off
REM This script demonstrates how to set up the project using uv package manager on Windows

REM Check if uv is installed
pip show uv >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo uv is not installed. Installing uv...
    pip install uv
)

echo Creating virtual environment with uv...
uv venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies with uv...
uv pip install -e .

echo Setup complete! You can now run the crawler with: python crawler.py
echo To activate this environment in the future, run: .venv\Scripts\activate.bat

pause