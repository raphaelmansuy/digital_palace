
# Today I Learned: Self-Installing Python Executables with UV

**Source:** [UV Documentation](https://github.com/astral-sh/uv)  

---

## Key Takeaways 🧠

### 1. **Shebang Magic**
```python
#!/usr/bin/env -S uv run
```
- First line tells OS to use `uv` as the script interpreter
- `-S` splits arguments to bypass shebang limitations
- Automatically handles dependency installation and environment setup

### 2. **Inline Metadata Block**
```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests", "rich"]
# ///
```
- PEP 723-compliant dependency declaration
- Supports Python version constraints
- Located immediately after shebang for automatic detection

### 3. **Zero-Install Execution**
```bash
./my_script.py  # Installs deps on first run, reuses after
```
- Creates `.uv-venvs` directory automatically
- Installs Python version if missing
- Builds isolated virtual environment

---

## Implementation Steps 🛠️

1. **Create Script**
```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pandas"]
# ///

import pandas as pd
print("Data analysis ready!")
```

2. **Make Executable**
```bash
chmod +x analysis_tool.py
```

3. **Run Anywhere**
```bash
# First run installs dependencies
./analysis_tool.py → auto-creates venv

# Subsequent runs use cached environment
./analysis_tool.py → instant startup
```

---

## Advanced Features 🔥

### Cross-Platform Execution
```python
#!/usr/bin/env -S uv run --python 3.11
```
- Forces specific Python version
- Handles Windows/macOS/Linux path differences

### Dependency Pinning
```python
# [tool.uv]
# resolution = "highest"
# exclude-newer = "2024-12-31"
```
- Locks dependency versions for reproducibility
- Prevents breaking changes

---

## Why This Matters 💡

1. **Portability**  
   Scripts become self-contained installers - no manual `pip install` needed

2. **Isolation**  
   Automatic per-script virtual environments prevent dependency conflicts

3. **DevOps Friendly**  
   `uv` installs dependencies 10-100x faster than traditional tools

---

## Try It Yourself ▶️
```bash
# Create demo script
echo '#!/usr/bin/env -S uv run\n# /// script\ndependencies=["pyjokes"]\n///\nimport pyjokes\nprint(pyjokes.get_joke())' > joke.py

# Make executable and run
chmod +x joke.py && ./joke.py
```

**Output:**  
`"What do you call a fake noodle? An Impasta."` *(via pyjokes)*


Or with this example on Mac that install an LLM:

```python
#!/usr/bin/env -S uv run
  
# /// script
# requires-python = ">=3.12"
# dependencies = ["mlx_lm"]
# ///

  
from mlx_lm import load, generate

  
model, tokenizer = load("mlx-community/Starling-LM-7B-beta-4bit")

response = generate(model, tokenizer, prompt="hello", verbose=**True**
```


---

## Pro Tip 💡
Add scripts to your PATH for global access:
```bash
mv joke.py ~/.local/bin/joke
joke  # Run from anywhere!
```

This workflow revolutionizes Python script distribution by combining the simplicity of shell scripts with Python's rich ecosystem. 🚀
