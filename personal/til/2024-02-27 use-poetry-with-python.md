# TIL: Mastering Poetry for Python Dependency Management (2024-02-27)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Effortless Python dependency management** – Use Poetry to create, manage, and distribute Python projects with isolated environments and reproducible builds.

---

## The Pain Point

Managing Python dependencies and environments manually is error-prone and leads to version conflicts. Poetry solves this by automating environment creation, dependency resolution, and packaging.

---

## What is Poetry?

Poetry is a Python dependency management tool that simplifies the creation, management, and distribution of Python projects. It ensures that each project has its own isolated environment, which prevents version conflicts and enhances reproducibility.

For a basic introduction to Poetry, refer to the [official documentation](https://python-poetry.org/docs/basic-usage/).

---

## Step-by-Step Guide

### 1. Install Poetry

```bash
pipx install poetry
```

### 2. Create a New Project

```bash
poetry new poetry-demo
```

### 3. Specify Python Version

In `pyproject.toml`:

```toml
python = "^3.7"
```

### 4. Configure Local Virtual Environment

```bash
poetry config virtualenvs.in-project true
poetry install
```

### 5. Activate the Virtual Environment

```bash
poetry shell
```

Or for Bash/Zsh:

```bash
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 6. Managing Dependencies

To add a library:

```bash
poetry add numpy
```

To remove a library:

```bash
poetry remove numpy
```

### 7. Building and Packaging

Create a `main.py` in the `poetry_demo` folder and define an entry point in `pyproject.toml`:

```toml
[tool.poetry.scripts]
poetry_demo = "poetry_demo.main:main"
```

Build the package:

```bash
poetry build
```

Install your package:

```bash
pipx install .
```

---

## Troubleshooting

- If dependencies aren’t installing, check your `pyproject.toml` for typos and ensure you’re using the correct Python version.
- If the virtual environment isn’t created, verify your Poetry config with `poetry config --list`.
- For advanced usage, see the [Poetry documentation](https://python-poetry.org/docs/).

---

## Security Considerations

- Never commit sensitive data or secrets to your `pyproject.toml` or `.env` files.
- Always use isolated environments to avoid dependency conflicts.
- Keep Poetry and Python up to date to avoid vulnerabilities.

---

## Related Resources

- [Poetry Official Documentation](https://python-poetry.org/docs/)
- [Poetry GitHub Repository](https://github.com/python-poetry/poetry)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

---

*⚡ Pro tip: Use `poetry export` to generate a requirements.txt for compatibility with other tools and CI/CD pipelines!*
