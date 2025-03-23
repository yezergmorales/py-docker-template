# py-docker-template

Py-docker-template built using uv, which is an extremely fast Python package and project manager, written in Rust. It aims to simplify project setup, streamline dependency management, and promote best practices for Python development

## Dependencies

uv is a single command line executable. There are a number of ways to install it, but the easiest is to use the provided installation script:

```console
# Windows
# probably it is needed to deactivate Windows Defender or antivirus
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
$env:Path = "C:\Users\your_user\.local\bin;$env:Path"

# MacOS
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

uv commands
```console
# Create a .venv with uv
# modify pyproject.toml whether is needed
uv run

# Update the project’s environment
uv sync 

# Add dependencies to your `pyproject.toml` with the uv add command. 
uv add 'requests==2.31.0'
uv add make

# Add a git dependency
uv add git+https://github.com/psf/requests

# To remove a package, you can use uv remove:
uv remove requests
```

How to use uv to execute your script?
```console
$ uv run src\services\hello_world_service.py 
Hello world
```

## Using Ruff and MyPy

Ruff is already in pyproject.toml
```console
ruff check                          # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.
ruff check @arguments.txt           # Lint using an input file, treating its contents as newline-delimited command-line arguments.
```
MyPy can be used as a VSCode extension

## Tests

Run the tests in cmd
```console
pytest tests/
```


