# Palt

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/DF5HSE/Designing2021?include_prereleases)
<!--
![GitHub last commit](https://img.shields.io/github/last-commit/DF5HSE/Designing2021)
![GitHub issues](https://img.shields.io/github/issues-raw/DF5HSE/Designing2021)
![GitHub pull requests](https://img.shields.io/github/issues-pr/DF5HSE/Designing2021)
![GitHub](https://img.shields.io/github/license/DF5HSE/Designing2021)
--> 


**Palt** is an application for reading books with interface for
commenting and discussion by quotes.

# Table of contents
- [Table of contents](#table-of-contents)
- [Roadmap](#roadmap)
- [Installation](#installation)
- [Usage](#usage)
    - [Build system](#build-system)
    - [Web application](#web-application)
- [Wiki](#wiki)
- [Authors](#authors)


# Installation
To run project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/DF5HSE/SE2021Practice.git```

Make sure you have Python3 and pip installed on your device. Perform installation
dependencies by running 

```python3 build-system-script.py install-depends```

<!--
You may run tests to check whether everyting is OK by running

```python3 build-system-script.py test```
-->

# Usage
## Build system
`build-system-script.py` -- is a script which help to run some routine
operations and checks automatically. You can launch it by:
`python3 build-system-script.py <command>`. Available commands are:
- `install-depends` -- install dependencies, listed in `requirements.txt`.
- `type-check` -- run [mypy](https://mypy.readthedocs.io/en/stable/), which check matching
of types in source python files.
- `pylint` -- run [pylint](https://www.pylint.org/) linter above source files
- `all-checks` -- run all checks commands.
<!--
- `test` -- run tests.
- `check-coverage` -- check coverage of source files by tests.
-->

## Web application
You can launch web application on your local host by command:

`uvicorn src:palt_app --reload`

After that you can try out endpoints in your browser on
http://127.0.0.1:8000/docs

# Wiki
Documentation and other useful materials you can find in project
[wiki](https://github.com/DF5HSE/Designing2021/wiki).

# Project status
Project is in development. The first step is creating a web application,
which is in progress now.

# Roadmap
Roadmap for project can be found
[here](https://github.com/DF5HSE/Designing2021/projects/1).

# Author
Denis Filippov (GitHub: [DF5HSE](https://github.com/DF5HSE))

<!--
# License
[(Back to top)](#table-of-contents)
[MIT licenses](https://opensource.org/licenses/MIT)

# Footer
[(Back to top)](#table-of-contents)

Leave a star in GitHub and wait for upcomming updates and news!
-->





