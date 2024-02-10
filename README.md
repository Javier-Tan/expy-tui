# expy-tui
A general expenses tracking TUI 
- Built in Python 3.10.11
- TUI made with [Textual](https://github.com/Textualize/textual)
- Data stored with [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- Type checked by [pydantic](https://github.com/pydantic/pydantic)
- Linted by [Ruff](https://github.com/astral-sh/ruff)
- Tested by [pytest](https://github.com/pytest-dev/pytest)

## Running expy
Requirements can be found in `tools/requirements.txt`, and can be installed by running `pip install -r tools/requirements.txt`

However it is highly recommended to use venv to develop and run expy. 

A bash script has been made to setup the virtual environment on linux and install the requirements, simply run `source tools/_setup_venv.sh` from the home directory.

## Documentation
All documentation can be found in `docs/`