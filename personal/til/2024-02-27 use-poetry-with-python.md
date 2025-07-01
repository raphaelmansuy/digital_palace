# [![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)
# Mastering Poetry

## What is Poetry?

Poetry is a Python dependency management tool that simplifies the creation, management, and distribution of Python projects. It ensures that each project has its own isolated environment, which prevents version conflicts and enhances reproducibility.

For a basic introduction to Poetry, refer to the [official documentation](https://python-poetry.org/docs/basic-usage/).

### Getting Started with Poetry

#### 1. Install Poetry

To install Poetry, run the following command:

```bash
pipx install poetry
```

#### 2. Create a New Project

Create a new project using:

```bash
poetry new poetry-demo
```

This command sets up a new directory `poetry-demo` with the necessary project structure.

#### 3. Specify Python Version

In `pyproject.toml`, specify the Python version like so:

```toml
python = "^3.7"
```

#### 4. Configure Local Virtual Environment

To configure Poetry to create a local `.venv`:

```bash
poetry config virtualenvs.in-project true
```

Then, install dependencies and set up the `.venv` with:

```bash
poetry install
```

#### 5. Activate the Virtual Environment

Activate the virtual environment using:

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

#### 6. Managing Dependencies

To add a library:

```bash
poetry add numpy
```

To remove a library:

```bash
poetry remove numpy
```

#### 7. Building and Packaging

Create a `main.py` in the `poetry_demo` folder and define an entry point in `pyproject.toml`:

```toml
[tool.poetry.scripts]
poetry_demo = "poetry_demo.main:main"
```

Build the package with:

```bash
poetry build
```

Install your package using:

```bash
pipx install .
```
