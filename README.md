# Simple Bank Transaction Manager
[![Python Coveralls](https://github.com/zhuberty/simple-bank-transaction-manager/actions/workflows/coveralls.yml/badge.svg)](https://github.com/zhuberty/simple-bank-transaction-manager/actions/workflows/coveralls.yml) [![Coverage Status](https://coveralls.io/repos/github/zhuberty/simple-bank-transaction-manager/badge.svg?branch=main)](https://coveralls.io/github/zhuberty/simple-bank-transaction-manager?branch=main)

This free software project aims to empower the common person to categorize their bank transactions and gain simple but comprehensive insights into spending and earning over time.

## Status of the project
This project is in the early stages of development. It is not ready for use.

# How to Use
Download the latest release from the releases page. Run the executable file. Follow the instructions shown in the GUI or CLI.

## Screenshots
Coming soon...

## Experiencing Issues?
Describe the problem on the Issues page in GitHub for this project.

# Instructions for Software Developers
## Install Poetry
This is a convenient package manager for Python projects. It is used to install the dependencies for this project.

Follow the instructions here: https://python-poetry.org/docs/#installation


## Install the dependencies in a virtual environment using Poetry
Run the following command from the root project directory:
```poetry install```

## Tests
To run the tests, run the following command from the root directory:
```pytest```

## GitHub Actions
This project uses GitHub Actions to run the tests on every push to the main branch and produce a coverage report using coveralls. The workflow is defined in the file: ```.github/workflows/coveralls.yml```

Learn more about using Coveralls here https://coveralls.io/

## License
This project is licensed under the GPL-3.0 License - see the LICENSE file for details