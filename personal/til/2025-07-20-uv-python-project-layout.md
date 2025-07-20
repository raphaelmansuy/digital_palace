# TIL: My 2025 uv-based Python Project Layout for Production Apps (2025-07-20)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **From script to production, one tool to rule them all:** UV makes Python project setup, dependency management, and packaging fast, reproducible, and ergonomic. Here’s how to structure your project for success in 2025.

---

## The Pain Point

Historically, Python project setup and packaging was slow, error-prone, and confusing. Multiple tools, complex instructions, and platform-specific issues made onboarding and deployment a headache. In 2025, UV solves these problems with a single, fast tool.

---

## Step-by-Step Guide

### 1. Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create a Proper Package Layout

- Use an `src/` directory for your package code.
- Example structure:

```text
hello-svc/
├── src/
│   └── hello_svc/
│       ├── __init__.py
│       ├── views.py
│       ├── asgi.py
├── tests/
│   └── test_e2e.py
├── pyproject.toml
```

### 3. Define Entry Points

- For ASGI apps, create `asgi.py`:

```python
# src/hello_svc/asgi.py
from .views import app
```

- Keep entry points minimal; only bridge between the outside world and your app.

### 4. Add Project Metadata and Dependencies

- Use `pyproject.toml` for all metadata and dependencies:

```toml
[project]
name = "hello-svc"
version = "0"
requires-python = ">=3.13"
dependencies = [
    "fastapi",
    "granian",
    "stamina"
]

[project.optional-dependencies]
dev = [
    "pytest",
    "fastapi[standard]"
]

[build-system]
requires = ["uv"]
build-backend = "uv.build"
```

### 5. Run and Test with UV

- UV manages Python versions and virtualenvs automatically.
- Run tests:

```bash
uv run pytest
```

- Start the development server:

```bash
uv run fastapi dev src/hello_svc/asgi.py
```

### 6. Lock and Share Dependencies

- UV creates a cross-platform `uv.lock` file for reproducible builds.
- Commit `uv.lock` to version control.
- Add `.venv` to `.gitignore`.

### 7. Tips & Best Practices

- Prefer package layout (`src/`) for easier imports and fewer bugs.
- Use dependency groups for dev tools to avoid leaking dev dependencies into production.
- Entry points should be simple and only used for running the app.
- Use ASGI containers like Granian for production, FastAPI dev server for local development.
- Avoid Docker for local development; use it only for production packaging.
- Check in your lock file for stable deployments.
- Assign clear names to fixtures and entry points for maintainability.

---

## 📚 Resources

- [YouTube: My 2025 uv-based Python Project Layout for Production Apps](https://www.youtube.com/watch?v=mFyE9xgeKcA)
- [Hynek’s Blog: src layout pattern](https://hynek.me/articles/testing-packaging/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Granian ASGI Server](https://github.com/emmett-framework/granian)
- [PEP 735: Dependency Groups](https://peps.python.org/pep-0735/)
- [PEP 440: Version Specifiers](https://peps.python.org/pep-0440/)

---

**You now have a robust, ergonomic, and production-ready Python project layout using UV!**
