import pytest
from stopping_problem.candidate import candidate


def test_candidate():
    c = candidate(0.89)
    assert c.quality == 0.89

