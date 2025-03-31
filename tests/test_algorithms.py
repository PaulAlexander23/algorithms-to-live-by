import pytest
import numpy as np
from algorithmstolivebypaulalexander.algorithms import random_algorithm, optimal_stopping_algorithm
from algorithmstolivebypaulalexander.candidate import candidate
from algorithmstolivebypaulalexander.candidate_list import candidate_list

def test_random_algorithm():
    np.random.seed(0)
    a = random_algorithm()
    c = candidate_list(1)
    assert a.solve(c.candidates) == c.candidates[0]

def test_optimal_stopping_algorithm():
    a = optimal_stopping_algorithm()
    np.random.seed(0)
    c = candidate_list(10)
    assert a.solve(c.candidates) == c.candidates[7]



