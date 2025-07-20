# TIL: Making Local Python Workflows FAST and BORING with UV, Just, and Direnv (2025-07-20)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Automate, standardize, and speed up your Python development:** UV, justfile, and direnv together make local workflows ergonomic, reproducible, and team-friendly. Here’s how to tie it all together for production apps in 2025.

---

## The Pain Point

Python development used to be slow, error-prone, and hard to standardize. Multiple tools, manual steps, and platform quirks made onboarding and daily work a hassle. UV, just, and direnv solve these problems with fast, automated, and reproducible workflows.

---

## Step-by-Step Guide

### 1. Use UV for Dependency Management and Running Commands

- Run tests and servers with locked dependencies and correct Python version:

```bash
uv run pytest
uv run fastapi dev src/hello_svc/asgi.py
```

- Add dependencies:

```bash
uv add <package>
```

- Update all dependencies fast:

```bash
uv lock --upgrade
```

- Sync and create virtualenv:

```bash
uv sync
```

### 2. Automate Commands with Justfile

## What is Just?

**Just** is a modern command runner, similar to Make but focused on running tasks and scripts, not building software. Written in Rust, it’s fast, cross-platform, and lets you define recipes (commands) in a `justfile` for automation, testing, and development. Unlike Make, Just is easy to use on Windows, macOS, and Linux, and supports arguments, environment variables, and grouping recipes for clarity.

- Install just (see docs for your OS):

```bash
brew install just  # macOS
```

- Example justfile for common tasks:

```makefile
# justfile

# Run tests
recipe test:
    uv run pytest

# Run coverage
recipe cov:
    uv run pytest --cov

# Start dev server
recipe serve:
    uv run fastapi dev src/hello_svc/asgi.py

# Update dependencies
recipe update:
    uv lock --upgrade

# Sync virtualenv
recipe install:
    uv sync

# Clean and refresh
recipe fresh:
    rm -rf .venv
    uv sync
```

- Use shell aliases for frequent commands:

```bash
alias t='just test'
```

### 3. Manage Environments with Direnv

## What is Direnv?

**Direnv** is a shell extension that automatically loads and unloads environment variables when you enter or leave a directory. It reads configuration from a `.envrc` file, making it easy to activate virtual environments, set project-specific variables, and manage secrets. Direnv works with Bash, Zsh, Fish, and other shells, and is supported by popular IDEs for seamless environment management.

- Install direnv (see docs for your OS):

```bash
brew install direnv  # macOS
```

- Minimal `.envrc` for a UV project:

```bash
uv sync
layout python .venv
```

- Approve `.envrc`:

```bash
direnv allow
```

- Use `.env` for environment variables:

```env
PORT=12345
DEBUG=true
```

### 4. Organize and Document Recipes

- Group recipes in justfile for clarity (QA, run, deploy, setup, lifecycle).
- Add comments/docstrings above recipes for discoverability.
- Use private recipes (underscore prefix) for internal tasks.

---

## Tips & Best Practices

- Prefer `uv run -m` for running modules, especially with `--with` for extra dependencies.
- Use bottom pinning for dependencies to avoid versioning issues.
- Use environment variables and dotenv files for flexible configuration.
- Use just for cross-platform command automation instead of makefiles.
- Use direnv for automatic virtualenv activation and environment management.
- Keep workflows standardized and automated for easier onboarding and teamwork.
- Use recipes for common tasks: test, cov, lint, typing, serve, req, browser, update, install, fresh.
- Organize recipes and use comments/docstrings for discoverability.

---

## Latest Best Practices & Updates (2025)

- **Legacy venv compatibility:** Use `uv venv` to bridge old and new workflows, making migration easier.
- **Docker integration:** UV dramatically speeds up Docker builds and dependency installation. See [ROX Automation Docker Best Practices](https://docs.roxautomation.com/linux/docker_best_practices/).
- **Bottom pinning:** UV’s default bottom pinning for dependencies is now recommended for reproducibility and security.
- **Inline dependencies:** Use UV’s inline dependencies for quick prototyping in single-file scripts.
- **IDE integration:** UV and direnv are now supported in VS Code, PyCharm, and Zed for seamless environment management.
- **Justfile tips:** Group recipes, use comments/docstrings, and leverage private recipes (underscore prefix) for internal tasks and discoverability.

---

## 📚 Resources

- [YouTube: uv - Making Local Python Workflows FAST and BORING in 2025](https://www.youtube.com/watch?v=TiBIjouDGuI)
- [UV Documentation](https://github.com/astral-sh/uv)
- [UV Changelog](https://github.com/astral-sh/uv/blob/main/changelogs/0.5.x.md)
- [Just Documentation](https://github.com/casey/just)
- [Direnv Documentation](https://direnv.net/)
- [ROX Automation: Docker Best Practices](https://docs.roxautomation.com/linux/docker_best_practices/)
- [PyCon US 2025: Virtualenvs & UV](https://us.pycon.org/2025/)

---

**You now have a fast, automated, and reproducible Python workflow for local development and production!**
