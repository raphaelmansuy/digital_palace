# [![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](../README.md)
# Python Package Management with Pip and Conda

## Information

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 28/09/2023 | 28/09/2023 | 1.0.0   |

Python has a vast ecosystem of open source libraries and packages that make it easier to perform common tasks like data analysis, machine learning, web development, etc. Managing these packages and their dependencies can get complicated, which is why tools like `pip` and `conda` are so useful!

## Step 1 - Install Pip

Pip is the standard package manager for Python. It is usually installed by default with Python, but you can check if you have it by running:

```
pip --version
```

If pip is not installed, you can install it by running:

```
python -m ensurepip --default-pip
```

## Step 2 - Install Packages with Pip

To install a package with pip, run:

```
pip install <package-name>
```

For example, to install the popular NumPy package:

```
pip install numpy
```

Pip will download the package and its dependencies and install them in your Python environment.

## Step 3 - Manage Virtual Environments with Conda

Conda is another powerful package manager that is commonly used for data science and machine learning projects. Conda makes it easy to create separate virtual environments so different projects can have isolated dependencies.

First, install Conda if you don't already have it. Then create a new environment:

```
conda create --name myenv
```

Activate the environment:

```
conda activate myenv
```

Now any packages installed will be isolated in the `myenv` environment. You can install packages with `conda` or `pip`.

## Step 4 - Export Environment File

To share your Conda environment settings with others, export the installed packages to a YAML file:

```
conda env export > environment.yml
```

The `environment.yml` file lists all packages and versions for that environment. Others can recreate the same environment from this file.

## Step 5 - Managing Environments and Packages

Pip and Conda give you powerful tools to install and manage Python packages. Some key commands:

- `pip install` - Install Python packages with pip
- `conda create` - Create new virtual environments
- `conda activate` - Activate an environment
- `conda env export` - Export conda environment settings

Using virtual environments and managing dependencies with pip and conda is crucial for Python development!
