# Variables
PYTHON = python
VENV = .venv
ACTIVATE = . $(VENV)/bin/activate

# Targets
.PHONY: setup test clean

# Set up a virtual environment and install dependencies
setup:
	@echo "Setting up the virtual environment..."
	@if [ ! -d "$(VENV)" ]; then $(PYTHON) -m venv $(VENV); fi
	@$(ACTIVATE) && pip install -r requirements.txt

# Run tests
test:
	@echo "Running tests in all test folders..."
	@$(ACTIVATE) && PYTHONPATH=src pytest --import-mode=importlib tests

# Clean up build artifacts
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +

