# Algorithms To Live By

This is a project containing my own python implementations of the problems and algorithms raised in the [Algorithms to live by](https://algorithmstoliveby.com/) book by Brian Christian and Tom Griffiths.
The aim of this project is to:
- Develop my python programming, including different data structures and python libraries and tools
- Understand the algorithms better by implementing them
- Have a simple project to experiment with CI/CD pipelines and good project practices
- Practise writing good documentation
- Implement test driven development

## Getting started

### Prerequisites

- Python 3.6 or later
- pip
- virtualenv

### Setup

Make is used to manage the project. To setup the project, run the following command:

```
make setup
```
This creates a virtual environment and installs the required python packages, see the [requirements.txt](requirements.txt) file.

### Running the tests

To run the tests, run the following command:

```
make test
```

### Running the code

To run the code, run the following command:

```
make FOLDER
```
where `FOLDER` is the folder containing the `main.py` you want to run.

### Cleaning up

To clean up the project, run the following command:

```bash
make clean
```
which removes the virtual environment and any other generated files.

## Contributing

You are more than welcome contribute by raising github issues (even just to ask questions, or raise a point) and/or submit a pull requests.
The standard github flow is used:
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Naturally, this project is inspired by and makes heavy use of the book [Algorithms to live by](https://algorithmstoliveby.com/) by Brian Christian and Tom Griffiths.
