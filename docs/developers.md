# Developers guide
## Developing expy
Requirements can be found in `tools/requirements.txt`, and can be installed by running `pip install -r tools/requirements.txt`

However it is highly recommended to use venv to develop expy. 

A bash script has been made to setup the virtual environment on linux and install the requirements, simply run `source tools/_setup_venv.sh` from the home directory.

## Developer notes
- Docstrings are written in [Google docstring style](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)

## TODO List
### Pending / backlog

- [ ] Add category tests
- [ ] Write steps to run expy in README.md
- [ ] Implement TUI
  - [ ] Design TUI
  - [ ] Integrate with backend
- [ ] Update tests to make integration tests independent (TransactionCRUD)
- [ ] Add ability to reorder / delete / mass change trnsaction_categories

### In Progress

### Done ✓
- [x] Implement Transaction and CRUD backend
- [x] Add logging + traceback (TransactionCRUD)