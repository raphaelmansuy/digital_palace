# [![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](../README.md)
# Poetry - A Pythonista's Best Friend

## Information

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 28/09/2023 | 28/09/2023 | 1.0.0   |
| Raphaël MANSUY | 15/11/2023 | 15/11/2023 | 2.0.0   |




# Introduction to Poetry

Poetry is a dependency management and packaging tool for Python that aims to simplify managing virtual environments, dependencies, and building and publishing Python packages. Some key benefits of Poetry compared to other tools like pip or pipenv include:

- Isolates dependencies on a per-project basis to avoid conflicts[4]
- Declarative dependency management using pyproject.toml
- Resolves dependencies and installs compatible versions automatically
- Integrated building and packaging of projects
- Publishing packages to PyPI or private repositories

In this tutorial, we will cover installing Poetry on MacOS, creating Poetry projects, managing virtual environments, dependencies, packaging, publishing, and more. 

## Installing Poetry

Poetry provides an installation script to install the latest stable release. To install Poetry on MacOS, run:

```
curl -sSL https://install.python-poetry.org | python3 -
```

This will install Poetry into your user local binaries. Make sure `~/.local/bin` is on your `PATH` environment variable. 

To verify Poetry installed correctly, run:

```
poetry --version
```

You can also configure Poetry's settings with: 

```
poetry config --list
```

## Creating a New Poetry Project

To start a new Poetry project, navigate to the project directory and run:

```
poetry new my-project
```

This will create a `my-project` directory with the following files:

```
my-project
├── pyproject.toml
├── README.rst
├── my_project
│   └── __init__.py
└── tests
    ├── __init__.py 
    └── test_my_project.py
```

The `pyproject.toml` file declares all dependencies and settings for your project. The `my_project` package contains your Python code. The `tests` folder includes example test cases.

## Activating the Virtual Environment

With your project created, activate the virtual environment: 

```
poetry shell
```

This spawns a new shell session with the project's virtual environment activated. Confirm it worked by checking the modified path:

```
echo $PATH 
```

By default, Poetry creates virtual environments in `./.venv`. To store environments together in a central location instead:

```
poetry config virtualenvs.in-project false
```

To deactivate the virtual environment, exit the shell session.

## Managing Dependencies

Poetry uses `pyproject.toml` to declare dependencies. To add a dependency like `requests`:

```
poetry add requests
```

This adds `requests` to `pyproject.toml` and installs it into the virtual environment. 

You can also specify version constraints:

```
poetry add "requests>=2.20" 
```

To update dependencies:

```
poetry update
```

This fetches the latest versions satisfying the constraints in `pyproject.toml`.

To remove dependencies:

```
poetry remove <package>
```

Poetry will resolve dependencies and conflicts automatically. If another package requires an older version of a dependency, Poetry will install the compatible version.

To view installed packages and versions:

```
poetry show --tree
```

## Building and Packaging

To build a wheel from your project: 

```
poetry build 
```

This compiles a distributable wheel file into `./dist`.

To build a source archive:

```
poetry build -f sdist
``` 

This creates a `.tar.gz` file containing your source code. Wheels provide pre-compiled bytecode while source archives contain raw source.

## Publishing Packages 

Poetry integrates with PyPI for publishing. First, configure your API token:

```
poetry config pypi-token.pypi <your-token>
```

Then publish your package:

```
poetry publish
```

This builds the package and uploads it to PyPI. You can also publish to private repositories.

To update a published package:

```
poetry publish --build
```

This rebuilds and re-uploads the latest version.

## Common Commands

Here are some common Poetry commands for quick reference:

- `poetry new <project>` - Create a new Poetry project
- `poetry add <package>` - Add a dependency
- `poetry update` - Update dependencies
- `poetry shell` - Spawn shell in virtual environment 
- `poetry run` - Run command in virtual environment
- `poetry build` - Build project package
- `poetry publish` - Publish package to PyPI

## Troubleshooting and Issues

Here are some common issues and solutions when working with Poetry:

**Dependency conflicts** - Poetry will automatically resolve conflicts between dependencies. You can use `poetry update --lock` to regenerate the lock file and re-resolve if needed.

**Old virtual environments** - Delete Poetry's `.venv` folder and any old virtual environments to rebuild from scratch.

**Import errors** - Make sure you activate the virtual environment before importing project modules.

**Publishing errors** - Check your PyPI API token is correct and you have permissions to publish the package name.

**Performance issues** - Try updating Poetry to the latest version or rebuild the virtual environment.

## Conclusion

In this comprehensive tutorial, we covered:

- Installing Poetry on MacOS
- Creating new projects
- Managing virtual environments 
- Declaring dependencies
- Packaging and building distributables 
- Publishing packages to PyPI
- Useful commands and troubleshooting tips

Key takeaways:

- Poetry provides robust dependency and environment management for Python
- `pyproject.toml` declaratively defines all project dependencies 
- Packages can be built and published with simple commands
- Virtual environments are automatically created and managed

Poetry simplifies many aspects of Python project management. With its simple commands and declarative configuration, you can boost your productivity when developing Python packages!

## Additional Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [PyPI Packaging Guide](https://packaging.python.org/) 
- [Poetry PyPI Publishing](https://python-poetry.org/docs/libraries/#publishing-to-pypi)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
