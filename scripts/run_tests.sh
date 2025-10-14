#!/bin/bash
# Debug-enabled script to run pytest with coverage
echo "Debug: Current directory: $(pwd)"
echo "Debug: Checking requirements.txt..."
ls -l requirements.txt || echo "Error: requirements.txt missing!"
echo "Debug: Checking src/tests/..."
ls -l src/tests/ || echo "Error: src/tests/ directory missing!"
echo "🚀 Running tests for Agentic AI Platform..."
pip install -r requirements.txt || echo "Error: Failed to install dependencies!"
echo "Executing pytest..."
pytest src/tests/ -v --cov=src --cov-report=html --cov-report=term-missing || echo "Error: pytest failed!"
echo "✅ Tests complete! Check htmlcov/index.html for coverage report."
