# Poetry

Poetry is like npm but for python, it has several features that pip doesn't have, which we will call out with (1), (2), etc.. We first need to install it per the [guide here](https://python-poetry.org/docs/#installing-with-pipx).

First, [install pipx](https://pipx.pypa.io/stable/installation/) via `$ brew install pipx && pipx ensurepath`. Then, `$ pipx install poetry`.

Optionally, enable auto completions by following [oh-my-zsh instructions](https://python-poetry.org/docs/#oh-my-zsh). Now, when you type `$ poetry r` then hit tab, it should show you auto completions.

First just create a plain python project using poetry, that is `$ poetry new <project_name>`. Let's use the same project name of `hello_poetry`. We will create another poetry project when incorporating fastapi so this name doesn't matter

(1). Pip doesn't support project creation like how poetry created 2 folders (`hello_poetry` and `tests`) and a `pyproject.toml` file.

Look at the `pyproject.toml` file, it's like a `package.json` file in npm. It has the project name, version, and dependencies.

(2). With poetry, you don't need to create a virtual environment, it creates it for you and "activates it" (not exactly, but just know that you don't need to do it manually).

```python
# project_name/main.py

def hello_world():
    return "Hello, world!"

if __name__ == "__main__":
    print(hello_world())

# tests/test_main.py
from project_name.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, world!"
```

Let's use poetry to add a package to our project. First, let's add a package called `pydantic_settings`. This is a helpful library used to manage configuration settings.

Run `$ poetry add pydantic_settings`. This will add the package to the `pyproject.toml` file and creates a `poetry.lock` file.

(3). Lock files are like `package-lock.json` files in npm, they lock the dependencies to specific versions. With pip, you obtain an inferior version of it by running `$ pip freeze > requirements.txt`.
