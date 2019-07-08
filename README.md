# ebr-board

[![Azure DevOps builds](https://img.shields.io/azure-devops/build/tomtomweb/GitHub-TomTom-International/5/master.svg)](https://dev.azure.com/tomtomweb/GitHub-TomTom-International/_build/latest?definitionId=5&branchName=master)
[![Azure DevOps tests](https://img.shields.io/azure-devops/tests/tomtomweb/GitHub-TomTom-International/5/master.svg)](https://dev.azure.com/tomtomweb/GitHub-TomTom-International/_build/latest?definitionId=5&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/tomtomweb/GitHub-TomTom-International/5/master.svg)](https://dev.azure.com/tomtomweb/GitHub-TomTom-International/_build/latest?definitionId=5&branchName=master)

[![PyPI - Version](https://img.shields.io/pypi/v/ebr-board.svg)](https://pypi.org/project/ebr-board/)
[![PyPI - License](https://img.shields.io/pypi/l/ebr-board.svg)](https://pypi.org/project/ebr-board/)
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/ebr-board.svg)](https://pypi.org/project/ebr-board/)
[![PyPI - Format](https://img.shields.io/pypi/format/ebr-board.svg)](https://pypi.org/project/ebr-board/)
[![PyPI - Status](https://img.shields.io/pypi/status/ebr-board.svg)](https://pypi.org/project/ebr-board/)
[![PyUp - Updates](https://pyup.io/repos/github/tomtom-international/ebr-board/shield.svg)](https://pyup.io/repos/github/tomtom-international/ebr-board/)


RESTful interface for Elastic Build Results.

## Usage

To view the API documentation, start the server and go to to `<url>/api/docs`.

### Dev Mode

To start in dev mode, run ` python ebr_board/ebr_board.py`

### Production Mode

Can be invoked with `ebr_board:create_app(config_filename='/etc/ebr-board/config.yaml', vault_config_filename='/etc/ebr-board/vault.yaml', vault_creds_filename='/etc/ebr-board/vault.yaml', load_certs=True, reverse_proxy=True)`, for example from Gunicorn. You should configure it behind a reverse proxy - for more details see
any guide on configuring Flask servers for deployment. A Dockerfile pre-configuring Gunicorn is available in the root of the repository.

## Features

* Provides abstraction to fetch:
    * a list of builds from a given job
    * tests from a given job
    * aggregations of tests failures

### Todo:

* Improve test coverage
* Fill in coverage of resources
* Expand aggregation/search functionality

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [tomtom-international/cookiecutter-python](https://github.com/tomtom-international/cookiecutter-python) project template.
