# Developers guide
## Developing expy
Requirements can be found in `tools/requirements.txt`, and can be installed by running `pip install -r tools/requirements.txt`

However it is highly recommended to use venv to develop expy. 

A bash script has been made to setup the virtual environment on linux and install the requirements, simply run `source tools/_setup_venv.sh` from the home directory.

## TODO List
### Pending

- [ ] Write steps to run expy in README.md
- [ ] Implement TUI
  - [ ] Design TUI
  - [ ] Integrate with backend

### In Progress

- [ ] Develop Transaction / Transaction CRUD backend functionality
  - [x] Update design to break monolithic test_crud_sqlite test into smaller tests
  - [ ] Update tests to make integration tests independent
  - [ ] Add logging

### Done ✓