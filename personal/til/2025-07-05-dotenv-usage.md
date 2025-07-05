---
title: "Today I Learned: Using dotenv for Python Environment Management"
date: 2025-07-05
tags: [python, environment, dotenv, cli, til]
---

# Today I Learned: Using `dotenv` for Python Environment Management

Managing environment variables is a best practice for Python projects, especially when dealing with secrets, API keys, or configuration that should not be hardcoded. The [`python-dotenv`](https://pypi.org/project/python-dotenv/) package makes this easy and secure.

## What is `dotenv`?

[`python-dotenv`](https://github.com/theskumar/python-dotenv) reads key-value pairs from a `.env` file and sets them as environment variables. This is especially useful for local development and for following [12-factor app](https://12factor.net/config) principles.

## Quick Start

1. **Install the package:**

   ```bash
   pip install python-dotenv
   # For CLI support:
   pip install "python-dotenv[cli]"
   ```

2. **Create a `.env` file** in your project root:

   ```env
   API_KEY=your_api_key_here
   DEBUG=True
   ```

3. **Use in Python code:**

   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Loads variables from .env into os.environ
   import os
   print(os.getenv("API_KEY"))
   ```

## Using the CLI: `dotenv run`

You can run any Python script with environment variables loaded from `.env` using the CLI:

```bash
dotenv run -- python engine/azure_litellm_sample.py
```

This ensures all variables in `.env` are available to your script, without polluting your global environment.

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

## Best Practices

- **Never commit your `.env` file** if it contains secrets. Add `.env` to your `.gitignore`.

- Use variable expansion for DRY configs:

  ```env
  DOMAIN=example.org
  API_URL=https://${DOMAIN}/api
  ```
- For advanced usage, see the [official documentation](https://saurabh-kumar.com/python-dotenv/).

## References

- [python-dotenv on PyPI](https://pypi.org/project/python-dotenv/)
- [Official documentation](https://saurabh-kumar.com/python-dotenv/)
- [GitHub repository](https://github.com/theskumar/python-dotenv)

---

*This TIL is part of the [Today I Learned](../README.md) series in Digital Palace.*
