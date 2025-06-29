# Today I Learned: Setting Up Optional Dependencies in a Python Library with Poetry

Today, I made significant progress on my monolithic library project, **Quantlogic**. I wanted to simplify the installation process so that users could easily install optional modules, similar to how they might use `pip install quantalogic[db]`. Here’s a step-by-step breakdown of how I set up **Poetry** to manage my project and its dependencies efficiently.

## 1. Installing Poetry

First, I needed to install Poetry, a powerful tool for dependency management and packaging in Python. I used the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installation, I verified it with:

```bash
poetry --version
```

## 2. Initializing My Project

Next, I navigated to my **Quantlogic** project directory and initialized it with Poetry:

```bash
cd path/to/quantalogic
poetry init
```

This command guided me through setting up the project's metadata, creating a `pyproject.toml` file.

## 3. Modifying `pyproject.toml`

I opened the generated `pyproject.toml` file to define my project’s dependencies and optional modules. Here’s how I structured the file:

```toml
[tool.poetry]
name = "quantalogic"
version = "0.1.0"
description = "Quantlogic library for complex calculations"
authors = ["Your Name <you@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.8"  # Adjust according to your compatibility
numpy = "^1.21.0"
pandas = "^1.3.0"

[tool.poetry.extras]
db = ["sqlalchemy", "psycopg2"]  # Optional DB libraries
ml = ["scikit-learn", "tensorflow"]  # Another optional dependency group

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Explanation of Key Sections:
- **`[tool.poetry.dependencies]`**: Lists the main dependencies required for the library.
- **`[tool.poetry.extras]`**: Defines optional groups of dependencies that users can install individually, such as database support with `quantalogic[db]`.

## 4. Installing Dependencies

To set up my library with its dependencies, I used:

```bash
poetry install
```

For optional dependencies, I could specify:

```bash
poetry install --extras "db"
```

## 5. Preparing for Publishing

Once my setup was complete, I built my package to ensure everything was functioning correctly:

```bash
poetry build
```

When ready, I could publish my package to PyPI with:

```bash
poetry publish
```

## 6. Updating Installation Instructions

Finally, I updated my documentation (README.md) to guide users on how to install **Quantlogic**. Here are the instructions I included:

```
# Install the main library
pip install quantalogic

# Install the library with database support
pip install quantalogic[db]
```

## Conclusion

By setting up optional dependencies in my **Quantlogic** library using Poetry, I streamlined the installation process for users. This enhances the flexibility of my package, allowing users to customize their installation according to their needs. 

Today’s learning experience reaffirms the value of effective dependency management tools in Python development. I’m excited to continue refining my project!