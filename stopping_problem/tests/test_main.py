import pytest
from stopping_problem.main import main


def test_main():
    assert main() == 0


