
# TIL: Using dotenv for Python Environment Management (2025-07-05)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Easily manage secrets and configs in Python** – Use `python-dotenv` to load environment variables from a `.env` file for secure, flexible development.

---

## The Pain Point

Hardcoding secrets and config in Python projects is risky and inflexible. Managing environment variables manually is error-prone. `python-dotenv` solves this by loading variables from a `.env` file automatically.

---

## Step-by-Step Guide

### 1. Install the package

```bash
pip install python-dotenv
# For CLI support:
pip install "python-dotenv[cli]"
```

### 2. Create a `.env` file in your project root

```env
API_KEY=your_api_key_here
DEBUG=True
```

### 3. Use in Python code

```python
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env into os.environ
import os
print(os.getenv("API_KEY"))
```

### 4. Use the CLI: `dotenv run`

Run any Python script with environment variables loaded from `.env`:

```bash
dotenv run -- python engine/azure_litellm_sample.py
```

All variables in `.env` are available to your script, without polluting your global environment.

---

## More CLI Examples

- List variables:
  ```bash
  dotenv list
  ```
- Set a variable:
  ```bash
  dotenv set DEBUG True
  ```
- Show as JSON:
  ```bash
  dotenv list --format=json
  ```

---

## Best Practices

- **Never commit your `.env` file** if it contains secrets. Add `.env` to your `.gitignore`.
- Use variable expansion for DRY configs:
  ```env
  DOMAIN=example.org
  API_URL=https://${DOMAIN}/api
  ```

---

## Troubleshooting

- If variables aren’t loading, check your `.env` file for typos and ensure `load_dotenv()` is called before accessing variables.
- For advanced usage, see the [official documentation](https://saurabh-kumar.com/python-dotenv/).

---

## Related Resources

- [python-dotenv on PyPI](https://pypi.org/project/python-dotenv/)
- [Official documentation](https://saurabh-kumar.com/python-dotenv/)
- [GitHub repository](https://github.com/theskumar/python-dotenv)

---

*This TIL is part of the [Today I Learned](../README.md) series in Digital Palace.*
