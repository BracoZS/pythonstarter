# Format code using Black and isort
format:
	poetry run black .
	poetry run isort .

# Run Ruff linter with auto-fix
ruff:
	poetry run ruff check --fix .
	
# Run type checking with MyPy
typecheck:
	poetry run mypy .

# Run type checking with PyRight
pyright:
	poetry run pyright .

# Run both type checkers
typecheck-all: typecheck pyright

# Quick code quality check (format + ruff + mypy)
check: format ruff typecheck

# Thorough code quality check (format + ruff + mypy + pyright)
check-all: format ruff typecheck-all

# Demonstrate type checking errors with example file
demo-errors:
	@echo "Checking example_type_errors.py with MyPy:"
	@poetry run mypy example_type_errors.py || true
	@echo "\nChecking example_type_errors.py with PyRight:"
	@poetry run pyright example_type_errors.py || true

# Help documentation
help:
	@echo "Available commands:"
	@echo "  make format       - Format code with Black and isort"
	@echo "  make ruff         - Run Ruff linter with auto-fix"
	@echo "  make typecheck    - Check types with MyPy"
	@echo "  make pyright      - Check types with PyRight"
	@echo "  make typecheck-all - Check types with both MyPy and PyRight"
	@echo "  make check        - Run format, linting and MyPy"
	@echo "  make check-all    - Run format, linting, MyPy and PyRight"
	@echo "  make demo-errors  - Show type errors in the example file"

# Set default target
.DEFAULT_GOAL := help