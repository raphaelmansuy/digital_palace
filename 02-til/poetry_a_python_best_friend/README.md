# Poetry - A Pythonista's Best Friend

## Information

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 28/09/2023 | 28/09/2023 | 1.0.0   |

Want to become a Python pro? Meet Poetry, your new best friend for wrangling Python projects!

Poetry helps you effortlessly do things that once caused headaches for Pythonistas, like managing virtual environments, dependencies, and packaging. With Poetry by your side, you'll be shipping Python projects like a seasoned developer in no time!

Let's start by installing Poetry:

```
pip install poetry
```

Poetry uses a pyproject.toml file at the root of your project to store configuration. Let's create a new project so Poetry can generate this file for us:

```
poetry new my-awesome-project
```

This creates a my-awesome-project folder with pyproject.toml inside - Poetry's playground!

One of Poetry's best features is virtual environment management. When generating a new project, it automatically creates an isolated env just for that project!

Now let's add some dependencies to pyproject.toml:

```
[tool.poetry.dependencies]
numpy = "^1.22.3"
pandas = "^1.4.0"
```

Run `poetry install` and Poetry will install these into the project's virtual env. Now import and use them:

```python
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(5, 3))
print(data)
```

Poetry makes building and sharing your project a breeze. Just run `poetry build` and it packages everything up neatly.

Ready to publish to PyPI? Poetry handles metadata generation and building distributions - no sweat!

```
poetry publish
```

Poetry also supports managing multiple Python versions and has a ton of other handy commands. Check out the [Poetry docs](https://python-poetry.org/docs/) to learn more!

As you can see, Poetry is an essential tool for Pythonistas. With Poetry by your side, you'll wonder how you ever managed without it! Give it a try and see how Poetry can be a Python pro's best friend too.
