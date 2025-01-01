import pytest
from stopping_problem.candidate_list import candidate_list

import numpy as np

def test_candidate_list():
    np.random.seed(0)
    c = candidate_list(1)
    assert c.length == 1

    np.random.seed(0)
    expected = np.random.rand()
    assert c.candidates[0].quality == expected
    assert c.best.quality == expected



