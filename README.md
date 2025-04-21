# Python Starter Project

A basic Python starter project with configurations for code formatting, linting, and type checking.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Poetry](https://img.shields.io/badge/poetry-managed-blueviolet)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Type Checking**: Using `mypy` for static type checking
- **Code Formatting**: Using `black` and `isort` for consistent code style
- **Linting**: Using `ruff` for fast Python linting
- **IDE Integration**: Pre-configured settings for VS Code, PyCharm, and Emacs
- **Git Integration**: Pre-commit hooks to enforce code quality
- **Dependency Management**: Using Poetry for reliable dependency management

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Poetry (Python package and dependency manager)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-starter.git
   cd python-starter
   ```

2. Install Poetry (if not already installed):
   ```bash
   # On macOS/Linux
   curl -sSL https://install.python-poetry.org | python3 -

   # On Windows (PowerShell)
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Configure Poetry to store virtual environments in the project directory (optional but recommended):
   ```bash
   poetry config virtualenvs.in-project true
   ```

4. Install project dependencies (including development tools):
   ```bash
   poetry install
   ```

5. Activate the virtual environment (optional but useful):
   ```bash
   # Find the path to the virtualenv
   poetry env info --path

   # Activate it manually (Linux/macOS)
   source .venv/bin/activate

   # On Windows (cmd)
   .venv\Scripts\activate
   ```

   Once activated, you can use `python` or `python3` directly:
   ```bash
   python3 example/index.py
   ```

6. Set up pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

## Development Tools

### Type Checking with MyPy

Run static type checking:

```bash
poetry run mypy .
```

### Code Formatting

Format all Python files in the project:

```bash
# Format with Black and sort imports
poetry run black .
poetry run isort .
```

### Linting with Ruff

Run the linter on all Python files:

```bash
# Check and fix issues
poetry run ruff check --fix .
```

### All-in-one Code Quality Check

You can create a simple `Makefile` to combine formatting, linting, and type checking (cross-platform-friendly with GNU Make installed):

```makefile
format:
	poetry run black .
	poetry run isort .

lint:
	poetry run ruff check --fix .

typecheck:
	poetry run mypy .

check: format lint typecheck
```

Then run:
```bash
make check
```

## Git Integration

### Pre-commit Hooks

This project includes pre-commit hooks to ensure code quality. They will run automatically before each commit and block commits if there are any linting errors or type checking issues.

The pre-commit configuration is in the `.pre-commit-config.yaml` file.

To manually run all pre-commit hooks:

```bash
poetry run pre-commit run --all-files
```

## Project Structure

- `pyproject.toml` - Project configuration, dependencies, and tool settings
- `.mypy.ini` - Additional MyPy configuration for type checking
- `.pre-commit-config.yaml` - Git pre-commit hook configuration
- `.vscode/settings.json` - VS Code settings for Python development
- `mytypes.py` - Example type definitions
- `index.py` - Example Python file with type hints

## IDE Integration

### Visual Studio Code

The included `.vscode/settings.json` file will automatically configure VS Code to use the correct formatting and linting settings. Just install the Python extension and select the Poetry virtual environment as your Python interpreter.

### PyCharm

PyCharm has excellent support for Poetry. To set up:

1. Go to Settings → Project → Python Interpreter
2. Click on the gear icon and select "Add..."
3. Choose "Poetry Environment" and select your project directory
4. PyCharm will automatically detect and use Poetry for the project

### Emacs

For Emacs integration with Poetry, you can use the `poetry.el` package:

```elisp
(use-package poetry
  :ensure t
  :config
  (poetry-tracking-mode))
```

## Dependency Management

### Poetry Commands Quick Reference

```bash
# Add a runtime dependency
poetry add <package-name>

# Add a development dependency
poetry add --group dev <package-name>

# Update all dependencies
poetry update

# Update a specific package
poetry update <package-name>

# Export requirements
poetry export -f requirements.txt --output requirements.txt
poetry export --with dev -f requirements.txt --output dev-requirements.txt
```

If you have a `requirements.txt` file and you want to install those dependencies, run:

```bash
poetry add $(cat requirements.txt)
```

This will install those dependencies and add them to your `pyproject.toml` file.

## Testing (Optional)

You can add `pytest` or `unittest` for test coverage.

```bash
# Example with pytest
poetry add --group dev pytest

# Run tests
poetry run pytest
```

## Type Checking Examples

This repository includes an `example_type_errors.py` file that intentionally contains type errors to demonstrate how the configured linters and type checkers work. This file is excluded from pre-commit hooks.

To see type checking in action, run:

```bash
poetry run mypy example_type_errors.py
# or
poetry run pyright example_type_errors.py
```

## Continuous Integration (Optional)

You can use GitHub Actions (or any CI provider) to automate linting, type-checking and testing.

Example: `.github/workflows/ci.yml`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
