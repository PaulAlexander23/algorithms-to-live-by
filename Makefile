# Variables
PYTHON = python
VENV = .venv
ACTIVATE = . $(VENV)/bin/activate
SUBFOLDERS = $(shell find . -type d -not -path "./.*" -not -path "./__pycache__" -not -path "./$(VENV)")

# Targets
.PHONY: setup test clean $(SUBFOLDERS)

# Set up a virtual environment and install dependencies
setup:
	@echo "Setting up the virtual environment..."
	@if [ ! -d "$(VENV)" ]; then $(PYTHON) -m venv $(VENV); fi
	@$(ACTIVATE) && pip install -r requirements.txt


# Pattern rule to run main.py in the specified subfolder
$(SUBFOLDERS):
	@echo "Running main.py in subfolder: $@"
	@$(ACTIVATE) && $(PYTHON) $@/main.py

# Run tests
test:
	@echo "Running tests in all test folders..."
	@$(ACTIVATE) && pytest

# Clean up build artifacts
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +

