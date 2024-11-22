# codescanning
# Author - Nicholas Gulrajani 
Python project with CodeQL scanning setup.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Running Tests

```bash
python -m pytest tests/
```

## Security Scanning

This project uses GitHub CodeQL for security scanning. Check the Security tab in GitHub for results.
