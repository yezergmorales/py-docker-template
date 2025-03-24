# py-docker-template

Py-docker-template built using uv, which is an extremely fast Python package and project manager, written in Rust. It aims to simplify project setup, streamline dependency management, and promote best practices for Python development.

## FastAPI Implementation

This project uses FastAPI, a modern, fast web framework for building APIs with Python. The implementation includes:

- A root endpoint (`/`) that returns a "Hello World" message using a service layer pattern
- A health check endpoint (`/health`) that returns the API status
- Automatic API documentation available at `/docs` using Swagger UI
- Async request handling for improved performance
- Type hints for better code safety and IDE support

The FastAPI application is configured to run using uvicorn server on port 8000, making it accessible via localhost.

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
.venv\Scripts\activate (whether activation is needed)

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

How to execute the APP using docker?
0. Docker desktop running
1. Create a requirements.txt in py-docker-template directory
```console
$ uv pip list --format=freeze > requirements.txt
```
2. Create Docker defaults inside of py-docker-template directory
```console
$ docker init
? What application platform does your project use? Python
? What version of Python do you want to use? 3.12.9
? What port do you want your app to listen on? 8000
? What is the command to run your app? uvicorn 'src.my_package.main:app' --host=0.0.0.0 --port=8000
```
3. Run the application
```console
$ docker compose up --build
$ docker compose up --build -d [Running in the background detached from the terminal]
# Open a browser and view the application at http://localhost:8000
```
3.1 Run the application in the virtual environment
```console
$ uvicorn src.my_package.main:app
# Open a browser and view the application at http://localhost:8000
```
4. Tip: Use Dev Containers to develop.
Make sure devcontainer.json has "remoteUser": "root"

APP access
```console
Main endpoint: http://localhost:8000/
Health check: http://localhost:8000/health
API documentation: http://localhost:8000/docs
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


