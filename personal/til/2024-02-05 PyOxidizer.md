
# TIL: PyOxidizer – Package Python Apps as Standalone Binaries (2024-02-05)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Package Python apps as single-file executables** – Use PyOxidizer to embed Python interpreter and dependencies in portable binaries that work on any machine without installation.

---

## The Pain Point

Packaging Python apps for distribution is notoriously hard—dependency hell, missing interpreters, and platform quirks make deployment complex and unreliable.

---

## Step-by-Step Guide

### 1. Install PyOxidizer

Install via pip or Rust:

```bash
python3 -m pip install pyoxidizer
# Or upgrade
python3 -m pip install --upgrade pyoxidizer
```

Or with Rust for latest version:

```bash
cargo install pyoxidizer
# Or from GitHub
cargo install --git https://github.com/indygreg/PyOxidizer.git --branch main pyoxidizer
### 2. Create a New Project

Initialize a PyOxidizer project:

```bash
pyoxidizer init-config-file my_python_app
cd my_python_app
```

This creates a `pyoxidizer.bzl` config file and project structure.

### 3. Configure Your Application

Open `pyoxidizer.bzl` and set what your app should run:

```python
python_config.run_command = "exec(open('main.py').read())"
```

Add dependencies with `pip_install`:

```python
for resource in exe.pip_install(["requests"]):
    resource.add_location = "in-memory"
    exe.add_python_resource(resource)
```

### 4. Build the Executable

Build your standalone binary:

```bash
pyoxidizer build
# Result is in the build/ directory
```

### 5. Package All Dependencies

To include all libraries from `requirements.txt`:

Generate requirements file:

```bash
pip freeze > requirements.txt
```

Edit `pyoxidizer.bzl` to include all packages:

```python
with open("requirements.txt", "r") as reqs:
    packages = [line.strip() for line in reqs if line.strip()]
for package in packages:
    for resource in exe.pip_install([package]):
        resource.add_location = "in-memory"
        exe.add_python_resource(resource)
```

---

## Troubleshooting

- Ensure your Python application is compatible with Python 3.8-3.10
- Verify your OS is supported (Windows, macOS, Linux on specified architectures)
- Check the [FAQ](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_faq.html) for common issues
- Use `pyoxidizer --help` for command-line options and debugging

---

## Related Resources

- [PyOxidizer Documentation](https://pyoxidizer.readthedocs.io/en/stable/)
- [Getting Started Guide](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_getting_started.html)
- [Configuration Reference](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_config.html)
- [GitHub Repository](https://github.com/indygreg/PyOxidizer)

---

*PyOxidizer lets you ship Python apps as fast, portable binaries—no more dependency hell!*

3. **Build the Executable:**
   After modifying the `pyoxidizer.bzl` file, you can build the executable with the included dependencies:

   ```bash
   pyoxidizer build
   ```

   This will create a standalone executable with all the dependencies from `requirements.txt` embedded within it.

