

# [![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

### Prepare Your Package for Distribution

1. **Ensure your `pyproject.toml` is complete**: This file should contain all the necessary metadata about your package, including the name, version, author, and any dependencies.

2. **Write a comprehensive `README.md`**: This file should include an introduction to your package, installation instructions, usage examples, and any other relevant information for users.

3. **Include a `LICENSE` file**: This file should contain the full text of the license under which you are releasing your package. You've chosen the MIT License, which is already included in your `LICENCE.md`.

4. **Ensure your package has a version number**: Follow semantic versioning. It looks like your `pyproject.toml` already specifies a version (`version = "0.1.3"`).

5. **Create a source distribution and wheel**: Run `poetry build` to create the distribution files. This will generate a `.tar.gz` file and a `.whl` file in the `dist` directory.

### Publish Your Package to PyPI

1. **Register an account on PyPI**: If you don't already have one, create an account on [PyPI](https://pypi.org/).

2. **Install Twine**: Twine is a utility for publishing Python packages on PyPI. You can install it using pip:

   ```bash
   pip install twine
   ```

3. **Upload your package**: Use Twine to upload your distribution files to PyPI:

   ```bash
   twine upload dist/*
   ```

   You will be prompted to enter your PyPI username and password.

4. **Verify the upload**: Once the upload is complete, you should be able to see your package listed on PyPI, and it should be installable via pip:

   ```bash
   pip install your-package-name
   ```

### Automate Package Deployment with GitHub Actions

You can automate the deployment of your package to PyPI using GitHub Actions whenever you push a new tag to your repository. Update your `.github/workflows/build.yml` file to include a step for publishing to PyPI:

```yml
    - name: Publish to PyPI
      if: startsWith(github.ref, 'refs/tags')
      uses: pypa/gh-action-pypi-publish@v1.4.2
      with:
        user: __token__
        password: ${{ secrets.PYPI_API_TOKEN }}
```

Before using this GitHub Action, you'll need to:

1. **Create a PyPI API token**: Log in to PyPI, go to your account settings, and create an API token with the necessary permissions to upload packages.

2. **Add the API token to your GitHub repository secrets**: Go to your repository settings on GitHub, find the "Secrets" section, and add your PyPI API token as a new secret (e.g., `PYPI_API_TOKEN`).

With these steps, your package will be automatically published to PyPI whenever you push a new tag that starts with `v`, indicating a version (e.g., `v0.1.4`).

Remember to update your package version in `pyproject.toml` before tagging a new release to avoid conflicts on PyPI.

