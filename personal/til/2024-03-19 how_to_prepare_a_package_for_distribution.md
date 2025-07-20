# TIL: How to Prepare a Python Package for Distribution (2024-03-19)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Distribute Python packages to PyPI with automated workflows** – Learn to prepare, build, and publish Python packages using modern tools and GitHub Actions for seamless distribution.

---

## The Pain Point

Publishing Python packages manually is error-prone and time-consuming. Getting the metadata right, building distributions, and managing PyPI uploads requires proper setup and automation.

---

## Step-by-Step Guide

### 1. Prepare Your Package for Distribution

Ensure your `pyproject.toml` is complete with all necessary metadata:

```toml
[project]
name = "your-package-name"
version = "0.1.3"
description = "Brief package description"
readme = "README.md"
authors = [{name = "Your Name", email = "you@example.com"}]
license = {text = "MIT"}
dependencies = ["requests>=2.25.0"]
```

Write a comprehensive `README.md` with installation instructions and usage examples.

Include a `LICENSE` file with the full license text.

### 2. Build Distribution Files

Create source distribution and wheel files:

```bash
poetry build
# or with build tool
python -m build
```

This generates `.tar.gz` and `.whl` files in the `dist` directory.

### 3. Publish to PyPI

Install Twine for uploading:

```bash
pip install twine
```

Upload your package:

```bash
twine upload dist/*
```

Enter your PyPI username and password when prompted.

### 4. Verify Installation

Test that your package is installable:

```bash
pip install your-package-name
```

### 5. Automate with GitHub Actions

Create `.github/workflows/publish.yml` for automated publishing:

```yml
name: Publish to PyPI

on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@v1.4.2
      with:
        user: __token__
        password: ${{ secrets.PYPI_API_TOKEN }}
```

---

## Troubleshooting

- If upload fails, check your PyPI credentials and package name availability
- For build errors, ensure `pyproject.toml` follows PEP 621 standards
- Use TestPyPI first to validate your package: `twine upload --repository testpypi dist/*`
- See [Python Packaging Guide](https://packaging.python.org/) for detailed help

---

## Security Considerations

- Never publish secrets, credentials, or API keys in your package or repository.
- Use PyPI API tokens (not passwords) for automated publishing in CI/CD workflows.
- Review dependencies for vulnerabilities before publishing.
- Audit your code for sensitive information before release.

---

## Related Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [PyPI Documentation](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [GitHub Actions for Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

---

*⚡ Pro tip: Use TestPyPI to validate your package before publishing to the main PyPI repository!*

