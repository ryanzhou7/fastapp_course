# Fastapi template

## Intro

We will use the [FastAPI-template](https://github.com/s3rius/FastAPI-template) tool to generate our project.

### Poetry setup

To use this, we need to install poetry.

Poetry is like npm but for python, it has several features that pip doesn't have, install it per the [guide here](https://python-poetry.org/docs/#installing-with-pipx).

First, [install pipx](https://pipx.pypa.io/stable/installation/) via `$ brew install pipx && pipx ensurepath`.

Then, `$ pipx install poetry`.

### fastapi_template setup

Now that you installed poetry with pipx, install `fastapi_template` with `pipx install fastapi_template` and verify

`$ fastapi_template --version`

## Configuration 1.

You are ready to create the project now.

To create our project, with the most simple settings:

`$ fastapi_template -n fastapp --quiet --api-type rest --db none --orm none --ci none`

Explanation of flags used

- `-n fastapp`: Project name
- `--quiet`: don't ask me questions for extra options
- `--api-type rest`: this is for a restful api (as opposed to graphql)
- `--db none`: don't add a database
- `--orm none`: don't add an ORM like sqlalchemy
- `--ci none`: don't add continuous integration like github actions

If you see

> `Check with Ruff..........................................................Failed`

This is fine to ignore.

You can also run `$ fastapi_template --help` to see the other options we will add.

Open this folder with VScode.

This is the simplest version of the project we can generate, but it is still a lot of new code.

Hence, this will be the most difficult.

All subsequent generations with additional options will be much be easier to understand.

### Github repo setup

On github create a new repo called `fastapp`, do not add a readme, .gitignore, or any other files.

With these options you should see

> …or create a new repository on the command line

and the commands that are like

```bash
echo "# fastapp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<YOUR_USER_NAME>/fastapp.git
git push -u origin main
```

`$ cd fastapp` (what fastapi_template created)

Now run only these commands to push the code up. Don't forget to replace `<YOUR_USER_NAME>`

```bash
git init
git add -A
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<YOUR_USER_NAME>/fastapp.git
git push -u origin main
```

### Python version selection

Like with most repos, start with reading the `README.md` file at the repo root. Return here after you finish reading the section of "Poetry" (but don't execute those commands).

It tells you to run the projects with these commands.

```bash
poetry install
poetry run python -m fastapp
```

But, before we do this we want to use the correct version of python, which is `3.11`.

We know this because the `Dockerfile` says so

```Dockerfile
# Dockerfile
FROM python:3.11.4-slim-bullseye as prod
```

This dockerfile is how the app will run in prod, so it'd be ideal for our local dev environment to match it as close as possible.

We will learn about this Dockerfile later on.

Use mise to use python 3.11 for this project. Patch version above `> 3.11` versions such as `3.11.15` is fine even though the Dockerfile says `python:3.11.4-slim-bullseye`. The `X` of `3.11.X` means that there are bug fixes and no breaking changes.

Check your version: `$ python3 --version`

If this doesn't match `3.11` you can run `source ~/.zshrc` (which reloads the configuration file) then try again, or open a new terminal tab.

### Project installation

Once your python version is correct, return to the repo `README.md` to follow it's installation instructions:

```bash
poetry install
poetry run python -m fastapp
```

In the browser [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs) should show you swagger docs.

### Poetry vs pip

Let's learn a little more about poetry

[Poetry cheatsheet](https://gist.github.com/CarlosDomingues/b88df15749af23a463148bd2c2b9b3fb) is a helpful cheat sheet.

Compare and contrast pip and poetry below

| Pip command                                             | Poetry command                                     |
| ------------------------------------------------------- | -------------------------------------------------- |
| `python3 -m venv env # create a virtual environment`    | Not needed, but most similar is `poetry install`   |
| `source env/bin/activate # activate it`                 | Not needed, but most similar is `poetry shell`     |
| `pip list # show installed libs`                        | `poetry show`                                      |
| `pip install -r requirements.txt # install all recs`    | `poetry install # install all recs in poetry.lock` |
| `pip install fastapi # install one lib`                 | `poetry add fastapi`                               |
| `which python # points to the py in the activated venv` | `poetry run which python`                          |

The above table is sorted by `pip` commands you'd typically run from top to bottom. If you run the poetry commands in the same order, you will get errors because the poetry workflow is...

```bash
poetry install # create a virtual environment if one doesn't already exist and install all recs in poetry.lock
poetry show # show all installed

# you'll see that the venv is not in the repo root, but this is fine
poetry run which python # Note the location

# starts a shell for which we are in the virtual environment poetry
poetry shell
which python # matches the location above, we don't need to preface with $ poetry run anymore in the activate shell
```

### Return to README.md

Return to `README.md` of the project.

- Skip reading the "Docker" section
- Give "Project structure" a glance, not to understand all of this now, but to note that it can be used as a reference
- Read "Configuration", then return here

### Fast reload

You currently have

```bash
# .env
FASTAPP_RELOAD=True
```

This flag is for local development, when you run `$ poetry run python -m fastapp`

Then make this change

```python
# /web/application.py
    # ...
    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    print("changed") # Add this
    return app
```

You'd expect to see the print and it should

However, there are exceptions to which files hot reload applies to.

Right now `http://localhost:8000/api/docs` should work.

Make this change and save the file

```python
# fastapp/settings.py
    # ...
    host: str = "127.0.0.1"
    port: int = 8001 # previously 8000
    # ...
```

In the terminal did you see:

> `WARNING:  WatchFiles detected changes in 'fastapp/settings.py'. Reloading...`

Does `http://localhost:8000/api/docs` still work? It should.

That is unexpected right? We changed the port from 8000 -> 8001.

Use control + c to kill the python command and run the app again.

Now `http://localhost:8000/api/docs` shouldn't work, but `http://localhost:8001/api/docs` does.

So, there are limitations to the auto-reload. But luckily, they are mostly edges cases.

The app does run on `8001` because fast reload is not smart enough to kill the app and restart it.

Test to see if `__main__.py` is also an edge case.

Solution: It is

### Debugger setup

We will now see the sequence of execution when we run the app.

We can add print statements, but it is easier / faster via the debugger.

Plus, setting up a debugger is extremely useful, you can pause execution and see local variables.

First find out the poetry virtual environment path with `$ poetry run which python`

For example. `/Users/<YOUR_USER>/Library/Caches/pypoetry/virtualenvs/fastapp-ZkIpIdmY-py3.10/bin/python`

Create a `.vscode` directory at the repo root add the following files

```json
// settings.json
{
  "python.pythonPath": "<INSERT_PATH>"
}

// launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: run poetry",
      "type": "python",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "module": "fastapp",
      "args": [],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

Now click in the top left and Run and Debug button, and the green run button.

The app should work as it previously did.

Look at the middle top for 6 buttons, which are:

| Action    | Icon |
| --------- | ---- |
| Continue  | ▶️   |
| Step Over | ⤵    |
| Step Into | ⬇️   |
| Step Out  | 🔼   |
| Restart   | ⭕️  |
| Stop      | ⏹    |

### Debugger breakpoints

Open `__main__.py` and click just left of the line numbers in line 1.

You should see "Click to add a breakpoint".

Do the same for line 1 of `fastapp/__init__.py`

Now we can see the first file that gets executed when we run the app.

Restart the debugger. Play around with the action buttons until you understand what each does.

### Execution sequence

This will be a long and complicate section, but it is import and will be worth it.

We will now go through each step of the execution sequence and get familiar with the files while we're at it.

Execution sequence is colloquially defined as, "where in the code are we currently at?"

1. We run `$ poetry run python -m fastapp`

- `-m` means we run the fastapp module
- the folder `fastapp` is a module because there is an `__init__.py` file
- This is generally true, to make a folder a module you must put an `__init__.py` file in that folder

2. `fastapp/__init__.py`

- The `__init__.py` file of a module is first to run. There is no executable code here.

3. `fastapp/__main__.py`

- `__main__.py` is a special name, it defines the entry point for the package when it is executed as a script.
- Since we ran with the `-m` flag command, Python looks for a `__main__.py` file within the package directory and executes it. This allows you to define what should happen when the package is run directly.

Now, we wil look at the files in detail. The step numbers (1. 2. 3.) still apply.

To be accurate to the execution sequence, we will have to have jump between files.

Fortunately, this will be noted. i.e. Now find step "# 15.".

Now, look for "# 4."

```python
# fastapp/__main__.py

# 4. This import uvicorn is run
import uvicorn

# 5. We import this file, find "# 6."
from fastapp.settings import settings

# 8. This code is defined
def main() -> None:
    """Entrypoint of the application."""
    # 10. we call this method
    uvicorn.run(
        # 11. We have referenced the fastapp module, fastapp/__init__.py is called again
        # find "# 12."
        "fastapp.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    ) # 22. Welcome back! You did it! See ## Execution sequence summary
    # We will actually never reach this area until uvicorn exits / fails / quits
    # So unless a shutdown is signaled, this method never returns
    # Look for "23. "

# 9. if statement below determines whether a Python script is being run as
# the main program or being imported as a module in another script.
if __name__ == "__main__":
    # this code will execute because this is run as a main program
    main()
```

```python
# fastapp/settings.py
# various imports here, won't go into depth...
# ...
# 6. This class is defined
class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """
    # ...
    reload: bool = False
    # ...

    # 8. At first the value of reload is False (above), but this code says
    # there is an .env file and read in variables with prefix "FASTAPP_"
    # after we read in this file (below), it overrides the above value as True
    """
    # .env file
    FASTAPP_RELOAD=True
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FASTAPP_",
        env_file_encoding="utf-8",
    )

# 7. Now we actually create an instance of this class
settings = Settings()
```

```python
# fastapp/web/application.py
# 12.
# Remember, this was imported via "fastapp.web.application:get_app"
# So actually # 12. is that web/__init__.py is executed but won't go into details there

# 13. These are lib import which are executed, but we disregard
from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

# 14. You know the drill by know...
# api is a module, it's __init__.py is executed, etc...
from fastapp.web.api.router import api_router
                    # 15. The code of the router.py file is executed, etc...
                    # continue below

# lifespan_setup.py is a file we have created, continue below
from fastapp.web.lifespan import lifespan_setup

def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    # 16. This method is actually invoked, because we got here from
    # "fastapp.web.application:get_app"
    app = FastAPI(
        # 17. This are run argument by argument
        title="fastapp",
        version=metadata.version("fastapp"),
        # 18. This is worth looking deeper into (see method lifespan_setup below)
        # BUT, this method is not actually run yet
        lifespan=lifespan_setup,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    return app
    # 19. After the app is returned it's ready to start up, so look for "20. "
    # 21. we're back in # fastapp/__main__.py, look for "22. "
```

```python
# fastapp/web/lifespan.py
# ...
@asynccontextmanager
async def lifespan_setup(
    app: FastAPI,
) -> AsyncGenerator[None, None]:  # pragma: no cover
    # Comments below are helpful!
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """
    # Code not run yet!! look for "19. "

    # 20. This is run now!
    app.middleware_stack = None
    app.middleware_stack = app.build_middleware_stack()
    # the yield keyword will pause the execution
    # Look for "22. "
    yield

    # 23. This is run after the app is shutdown
    # Typically you would put database clean up things here
    # i.e. if your app has crashed, it should disconnect from the db
    print("App has shutdown")
```

### Execution sequence summary

This summary is accurate as of now. As soon as imports change, it will not be.

Steps have been simplified and omitted

1. `$ poetry run python -m fastapp`
2. `fastapp/__init__.py`

- To load `fastapp` module

3. `fastapp/__main__.py`

- Because of the `-m` flag

4. `fastapp/settings.py` loads due to `from fastapp.settings import settings`
5. Back to `fastapp/__main__.py`

- `uvicorn.run()` is called
- `"fastapp.web.application:get_app",` is referenced

6. `fastapp/web/application.py`

- `get_app` invocation return is an app

7. App gets returned and starts up
8. Life cycle method is called
9. App shutsdown (error or manually)
10. Code after `yield` in `lifespan_setup` method of `fastapp/web/lifespan.py` file runs

That sequence was very complicated, but understanding is key as we add code to various portions of these steps.

### Health router sequence

Here's an easy execution sequence trace

By visiting [http://localhost:8000/api/docs](http://localhost:8000/api/docs) we can see the health endpoint

Which we can hit with `$ curl -X 'GET' 'http://localhost:8000/api/health' -H 'accept: application/json'`

```python
# fastapp/web/api/monitoring/views.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    print("hit")
```

When we do so the print is executed and we return from the method. None of the steps above come into play.

## Configuration 2.
