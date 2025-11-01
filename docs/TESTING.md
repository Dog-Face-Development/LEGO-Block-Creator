# Testing Guide

This document describes the testing infrastructure and practices for the LEGO Block Creator project.

## Test Suite Overview

The project includes a comprehensive test suite that covers all CLI commands and functionality with **100% code coverage**.

### Test Statistics

- **Total Tests**: 21
- **Code Coverage**: 100%
- **Test Framework**: pytest
- **Coverage Tool**: pytest-cov

## Running Tests

### Prerequisites

Install the required testing dependencies:

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest
```

This will automatically:
- Run all tests in the `tests/` directory
- Generate coverage reports (terminal, HTML, and XML)
- Display missing coverage lines

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Specific Tests

```bash
# Run a specific test file
pytest tests/test_main.py

# Run a specific test function
pytest tests/test_main.py::test_lego_cmd_newpiece
```

### View Coverage Report

After running tests, open the HTML coverage report:

```bash
# The report is generated in the htmlcov directory
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## Test Coverage

The test suite covers all CLI commands:

### Piece Management Commands
- `newpiece` - Create a new piece
- `newcolour`/`newcolor` - Create a new colour
- `addpiece` - Add quantity to existing piece
- `removepiece` - Remove quantity from piece

### Piece Sorting Commands
- `sortparts-all` - List all pieces
- `sortparts-name` - Search pieces by name
- `sortparts-colour`/`sortparts-color` - Filter by colour

### Set Management Commands
- `newset` - Create a new set
- `newtheme` - Create a new theme
- `addset` - Add quantity to existing set
- `removeset` - Remove quantity from set

### Set Sorting Commands
- `sortsets-all` - List all sets
- `sortsets-name` - Search sets by name
- `sortsets-number` - Search sets by number
- `sortsets-theme` - Filter by theme

### Utility Commands
- `help` - Display help information
- `copyright`/`license` - Display license information
- Invalid command handling

## Continuous Integration

### GitHub Actions Workflows

The project uses GitHub Actions for automated testing:

#### PyTest Workflow (`.github/workflows/pytest.yml`)

This workflow runs on every push and pull request:

- **Operating Systems**: Ubuntu, Windows, macOS
- **Python Versions**: 3.9, 3.10, 3.11, 3.12
- **Features**:
  - Installs dependencies
  - Runs full test suite
  - Generates coverage reports
  - Uploads coverage to Codecov (optional)

**Total Test Matrix**: 12 jobs (3 OS × 4 Python versions)

#### Pylint Workflow (`.github/workflows/pylint.yml`)

Ensures code quality standards:

- Runs on every push
- Analyzes all Python files
- Uses Python 3.9 as the base version

### Test Configuration

Test configuration is defined in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --strict-markers --cov=main --cov-report=term-missing --cov-report=html --cov-report=xml"
testpaths = ["tests"]
pythonpath = ["."]

[tool.coverage.run]
source = ["."]
omit = ["tests/*", "setup.py", "__main__.py"]
```

## Writing Tests

### Test Structure

Tests are located in the `tests/` directory and follow pytest conventions:

```python
from unittest.mock import patch, call
import main

@patch("builtins.input", side_effect=["command", "arg1", "arg2"])
@patch("builtins.print")
def test_lego_cmd_command(self, mock_print):
    """Test the command."""
    main.lego_cmd()
    mock_print.assert_has_calls([
        call("LEGO CMD: "),
        call("Expected output"),
    ])
```

### Test Guidelines

1. **Use descriptive test names**: Test names should clearly indicate what is being tested
2. **Mock user input**: Use `@patch("builtins.input")` to simulate user input
3. **Mock output**: Use `@patch("builtins.print")` to capture and verify output
4. **Test one command per test**: Each test should focus on a single CLI command
5. **Verify behavior**: Use assertions to verify expected behavior

## Troubleshooting

### Tests Fail Locally

1. Ensure you have the latest dependencies:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. Clear pytest cache:
   ```bash
   pytest --cache-clear
   ```

3. Check Python version:
   ```bash
   python --version  # Should be 3.9 or higher
   ```

### Coverage Issues

If coverage reports show unexpected results:

1. Delete existing coverage data:
   ```bash
   rm -rf .coverage htmlcov/ coverage.xml
   ```

2. Run tests again:
   ```bash
   pytest
   ```

## Contributing Tests

When contributing new features:

1. **Write tests first** (Test-Driven Development)
2. **Ensure 100% coverage** of new code
3. **Run pylint** to ensure code quality:
   ```bash
   pylint $(git ls-files '*.py')
   ```
4. **Verify tests pass** on your local machine before submitting a PR
5. **Update this documentation** if adding new test categories

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
