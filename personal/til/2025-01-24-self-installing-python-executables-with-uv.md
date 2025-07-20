
# TIL: Self-Installing Python Executables with UV (2025-01-24)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Distribute Python scripts with zero manual setup** – Use UV to create self-installing, portable Python executables that handle dependencies automatically.

---

## The Pain Point

Distributing Python scripts is a hassle: users must manually install dependencies, manage environments, and resolve version conflicts. UV solves this by making scripts self-installing and portable.

---

## Step-by-Step Guide

### 1. Shebang Magic

Add this to the top of your script:

```python
#!/usr/bin/env -S uv run
```

This tells the OS to use UV as the interpreter and bypasses shebang limitations.

### 2. Inline Metadata Block

Declare dependencies and Python version right after the shebang:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests", "rich"]
# ///
```

PEP 723-compliant, auto-detected by UV.

### 3. Zero-Install Execution

Make your script executable and run it:

```bash
chmod +x my_script.py
./my_script.py  # Installs deps on first run, reuses after
```

UV creates a `.uv-venvs` directory, installs Python if missing, and builds an isolated environment.

### 4. Advanced Features

- **Cross-Platform Execution:**

  ```python
  #!/usr/bin/env -S uv run --python 3.11
  ```

  Forces a specific Python version, works on Windows/macOS/Linux.

- **Dependency Pinning:**

  ```python
  # [tool.uv]
  # resolution = "highest"
  # exclude-newer = "2024-12-31"
  ```

  Locks dependency versions for reproducibility.

---

## Why This Matters

- **Portability:** Scripts become self-contained installers – no manual `pip install` needed.
- **Isolation:** Automatic per-script virtual environments prevent dependency conflicts.
- **DevOps Friendly:** UV installs dependencies 10-100x faster than traditional tools.

---

## Try It Yourself

Create a demo script:

```bash
echo '#!/usr/bin/env -S uv run\n# /// script\ndependencies=["pyjokes"]\n///\nimport pyjokes\nprint(pyjokes.get_joke())' > joke.py
chmod +x joke.py && ./joke.py
```
**Output:**
`"What do you call a fake noodle? An Impasta."` *(via pyjokes)*

Or try this example to install an LLM:
```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = ["mlx_lm"]
# ///

from mlx_lm import load, generate
model, tokenizer = load("mlx-community/Starling-LM-7B-beta-4bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```

---

## Troubleshooting

- If dependencies aren't installed, check the metadata block for typos.
- For cross-platform issues, ensure the shebang and Python version are correct.
- See [UV Documentation](https://github.com/astral-sh/uv) for more advanced usage.

---

## Related Resources

- [UV Documentation](https://github.com/astral-sh/uv)
- [PEP 723](https://peps.python.org/pep-0723/)
- [Python Packaging User Guide](https://packaging.python.org/)

---


*Pro Tip: Add scripts to your PATH for global access:*

```bash
mv joke.py ~/.local/bin/joke
joke  # Run from anywhere!
```

