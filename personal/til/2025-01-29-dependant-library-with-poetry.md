# TIL: Setting Up Optional Dependencies in a Python Library with Poetry (2025-01-29)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Streamline Python library installs with Poetry extras** – Use Poetry to define optional dependency groups for flexible, user-friendly installation.

---

## The Pain Point

Python libraries often require optional dependencies for features like database or machine learning support. Manual instructions are error-prone and confusing for users. Poetry makes this easy with extras.

---

## Step-by-Step Guide

### 1. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
```

### 2. Initialize Your Project

```bash
cd path/to/quantalogic
poetry init
```

### 3. Modify `pyproject.toml`

Define main and optional dependencies:

```toml
[tool.poetry]
name = "quantalogic"
version = "0.1.0"
description = "Quantlogic library for complex calculations"
authors = ["Your Name <you@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.8"
numpy = "^1.21.0"
pandas = "^1.3.0"

[tool.poetry.extras]
db = ["sqlalchemy", "psycopg2"]
ml = ["scikit-learn", "tensorflow"]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### 4. Install Dependencies

```bash
poetry install
poetry install --extras "db"
```

### 5. Build and Publish

```bash
poetry build
poetry publish
```

### 6. Update Installation Instructions

```bash
pip install quantalogic
pip install quantalogic[db]
```

---

## Troubleshooting

- If extras aren't working, check for typos in `[tool.poetry.extras]`.
- Make sure your `pyproject.toml` is valid TOML format.
- See [Poetry documentation](https://python-poetry.org/docs/) for advanced usage.

---

## Security Considerations

- Never commit sensitive data or secrets to your `pyproject.toml` or `.env` files.
- Always use isolated environments to avoid dependency conflicts.
- Keep Poetry and Python up to date to avoid vulnerabilities.

---

## Related Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [PEP 517/518](https://peps.python.org/pep-0517/)
- [Python Packaging User Guide](https://packaging.python.org/)

---

## Conclusion

By setting up optional dependencies in your library using Poetry, you make installation easier and more flexible for your users.

---

*⚡ Pro tip: Use Poetry extras to let users install only the features they need, keeping your library lightweight and flexible!*