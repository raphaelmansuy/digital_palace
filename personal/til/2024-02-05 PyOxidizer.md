

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

# PyOxidizer: Package Python Apps as Standalone Binaries

> **PyOxidizer** is a modern tool for packaging and distributing Python applications as single-file, portable executables. It leverages Rust to embed a Python interpreter and all dependencies, so your app "just works" on any supported machine.

---

## 🧩 What Problem Does PyOxidizer Solve?

Packaging Python apps for distribution is notoriously hard—dependency hell, missing interpreters, and platform quirks. PyOxidizer solves this by:
- Embedding a Python interpreter and all dependencies in a single binary
- Loading Python modules directly from memory (no temp files)
- Supporting Windows, macOS (Intel & ARM), and Linux
- Letting you focus on your app, not packaging headaches

---

## ⚙️ How Does It Work?

- Uses Rust to build binaries that embed Python and your code/resources
- Customizes Python distributions for minimal size and high portability
- Loads bytecode modules from memory using a high-performance importer
- Offers a flexible Starlark-based config file (`pyoxidizer.bzl`) to control builds

---

## 🚀 Getting Started

1. **Install PyOxidizer**
   - With pip (recommended):
     ```bash
     python3 -m pip install pyoxidizer
     # Or upgrade
     python3 -m pip install --upgrade pyoxidizer
     ```
   - Or with Rust (for latest/dev):
     ```bash
     cargo install pyoxidizer
     # Or from GitHub
     cargo install --git https://github.com/indygreg/PyOxidizer.git --branch main pyoxidizer
     ```

2. **Create a New Project**
   ```bash
   pyoxidizer init-config-file my_python_app
   cd my_python_app
   ```
   This creates a `pyoxidizer.bzl` config file and project structure.

3. **Edit the Config**
   - Open `pyoxidizer.bzl` and set what your app should run:
     ```python
     python_config.run_command = "exec(open('main.py').read())"
     ```
   - Add dependencies with `pip_install`:
     ```python
     for resource in exe.pip_install(["requests"]):
         resource.add_location = "in-memory"
         exe.add_python_resource(resource)
     ```

4. **Build the Executable**
   ```bash
   pyoxidizer build
   # Result is in the build/ directory
   ```

---

## 🏗️ Advanced Usage & Best Practices

- **Requirements:** Python 3.8–3.10, C compiler, supported OS (see docs)
- **Customizing:** Use the Starlark config to control entrypoints, resources, and packaging
- **Distributing:** PyOxidizer can build MSI installers (Windows), app bundles (macOS), and more
- **Troubleshooting:** See [FAQ](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_faq.html) and [Known Issues](https://github.com/indygreg/PyOxidizer/issues)
- **Performance:** Loads modules from memory for speed and security
- **Rust Integration:** You can embed Python in Rust apps, or incrementally rewrite Python in Rust

---

## 📦 Packaging All Dependencies (requirements.txt)

To include all libraries from `requirements.txt`:

1. Generate it:
   ```bash
   pip freeze > requirements.txt
   ```
2. Edit `pyoxidizer.bzl`:
   ```python
   with open("requirements.txt", "r") as reqs:
       packages = [line.strip() for line in reqs if line.strip()]
   for package in packages:
       for resource in exe.pip_install([package]):
           resource.add_location = "in-memory"
           exe.add_python_resource(resource)
   ```

---

## 🔗 Resources & Further Reading

- [PyOxidizer Documentation](https://pyoxidizer.readthedocs.io/en/stable/)
- [Getting Started Guide](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_getting_started.html)
- [Configuration Reference](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_config.html)
- [Packaging User Guide](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_packaging.html)
- [Distributing User Guide](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_distributing.html)
- [FAQ](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_faq.html)
- [GitHub Repo](https://github.com/indygreg/PyOxidizer)

---

**PyOxidizer lets you ship Python apps as fast, portable binaries—no more dependency hell!**

## How to Use PyOxidizer to Package a Simple Python Program

This tutorial will guide you through the process of using PyOxidizer to package a simple Python program. PyOxidizer is a utility that allows you to create a standalone executable from Python code, making distribution easier.

### Prerequisites

Before starting, ensure your Python application is compatible with Python 3.8, 3.9, or 3.10, as these are the versions PyOxidizer currently targets[1]. Also, verify that your operating system is supported (Windows, macOS, or Linux on specified architectures)[1] and that you have a working C compiler/toolchain installed[1].

### Installing PyOxidizer

PyOxidizer can be installed either from pre-built installers/executables or from source. For most users, installing the pre-built version is recommended:

```bash
python3 -m pip install pyoxidizer
# To upgrade an existing install
python3 -m pip install --upgrade pyoxidizer
```

If pre-built artifacts are not available for your platform, or if you prefer to install from source, ensure you have Rust (1.61 or newer) installed, then use `cargo` to install PyOxidizer:

```bash
cargo install pyoxidizer
# Or from the Git repository for the latest version
cargo install --git https://github.com/indygreg/PyOxidizer.git --branch main pyoxidizer
```

### Creating Your First PyOxidizer Project

1. **Initialize a New Configuration File**

   Start by creating a new PyOxidizer configuration file in your project directory:

   ```bash
   pyoxidizer init-config-file my_python_app
   ```

   This command creates a new directory `my_python_app` with a default PyOxidizer configuration file (`pyoxidizer.bzl`).

2. **Customize the Configuration**

   Open `my_python_app/pyoxidizer.bzl` in your editor. This file defines how your application is built and packaged. By default, it's configured to embed Python and start a REPL.

   To package your own Python program, modify the `python_config.run_command` line to execute your script. For example, to run a script named `main.py`, change it to:

   ```python
   python_config.run_command = "exec(open('main.py').read())"
   ```

   Ensure `main.py` is located in the `my_python_app` directory or adjust the path accordingly.

3. **Build and Run Your Application**

   Navigate to your project directory and build your application:

   ```bash
   cd my_python_app
   pyoxidizer build
   ```

   After the build completes, you can run your packaged application directly from the `build` directory.

### Packaging Additional Dependencies

If your application depends on external Python packages, you can use `pip_install` within the `pyoxidizer.bzl` file to include these. For example, to include the `requests` library:

```python
for resource in exe.pip_install(["requests"]):
    resource.add_location = "in-memory"
    exe.add_python_resource(resource)
```

### Conclusion

You've now learned how to use PyOxidizer to package a simple Python program into a standalone executable. This process simplifies the distribution of Python applications by removing the need for recipients to have a Python environment set up. For more advanced configurations and options, refer to the PyOxidizer documentation and the `pyoxidizer.bzl` file comments.

## FAQ

## How to include all the libraries from requirements.txt

To include all the libraries into a `requirements.txt` file with PyOxidizer, you would typically follow these steps:

1. **Generate a `requirements.txt` File:**
   If you don't already have a `requirements.txt` file, you can generate one using `pip freeze`:

   ```bash
   pip freeze > requirements.txt
   ```

   This command will create a `requirements.txt` file with all the libraries currently installed in your Python environment.

2. **Modify the PyOxidizer Configuration:**
   Open the `pyoxidizer.bzl` file in your PyOxidizer project and locate the function that defines the executable (often named `make_exe` or similar). You will need to modify this function to include the dependencies specified in your `requirements.txt` file.

   Here's an example of how you might modify the `pyoxidizer.bzl` file to include dependencies from `requirements.txt`:

   ```python
   def make_exe():
       dist = default_python_distribution()
       config = dist.make_python_interpreter_config()

       # Add each dependency from requirements.txt
       with open("requirements.txt", "r") as reqs:
           packages = [line.strip() for line in reqs if line.strip()]

       for package in packages:
           for resource in dist.to_python_executable().pip_install([package]):
               resource.add_location = "in-memory"
               dist.to_python_executable().add_python_resource(resource)

       # Set the initial run command for the Python interpreter
       config.run_command = "exec(open('your_script.py').read())"
       return dist.to_python_executable(config)
   ```

   In this example, the `make_exe` function reads the `requirements.txt` file and installs each package into the PyOxidizer executable using `pip_install`.

3. **Build the Executable:**
   After modifying the `pyoxidizer.bzl` file, you can build the executable with the included dependencies:

   ```bash
   pyoxidizer build
   ```

   This will create a standalone executable with all the dependencies from `requirements.txt` embedded within it.

