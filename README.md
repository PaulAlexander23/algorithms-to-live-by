# Algorithms To Live By

My own python implementations of the algorithms mentioned in the Algorithms to live by book.

What does this project do?
Why is this project useful?
How do I get started?
Where can I get more help, if I need it?

- Develop my python programming.
- Understand the algorithms better by implementing them.

# Getting started

## Prerequisites

- Python 3.6 or later
- pip
- virtualenv

## Setup

Make is used to manage the project. To setup the project, run the following command:

```bash
make setup
```
This creates a virtual environment and installs the required python packages, see the [requirements.txt](requirements.txt) file.

## Running the tests

To run the tests, run the following command:

```bash
make test
```

## Running the code

To run the code, run the following command:

```bash
make FOLDER
```
where `FOLDER` is the folder containing the `main.py` you want to run.

## Cleaning up

To clean up the project, run the following command:

```bash
make clean
```
which removes the virtual environment and any other generated files.

# Contributing

You are more than welcome contribute by raising github issues (even just to ask questions, or raise a point) and/or submit a pull requests.
The standard github flow is used:
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Acknowledgements

Naturally, this project is inspired by and makes heavy use of the book [Algorithms to live by](https://algorithmstoliveby.com/) by Brian Christian and Tom Griffiths.
