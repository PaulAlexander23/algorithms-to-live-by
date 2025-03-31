import pytest

from algorithmstolivebypaulalexander.sorting_problem import sorting_problem, searching_problem

def test_problem():
    p = sorting_problem(3)
    assert len(p.items) == 3
    assert p.items[0].name == "0"
    assert p.items[0].value >= 0
    assert p.items[0].value < 100
    assert p.items[1].name == "1"
    assert p.items[1].value >= 0
    assert p.items[1].value < 100
    assert p.items[2].name == "2"
    assert p.items[2].value >= 0
    assert p.items[2].value < 100

def test_search_problem():
    p = searching_problem(3, 50)
    assert len(p.items) == 3
    assert p.items[0].name == "0"
    assert p.items[0].value >= 0
    assert p.items[0].value < 100
    assert p.items[1].name == "1"
    assert p.items[1].value >= 0
    assert p.items[1].value < 100
    assert p.items[2].name == "2"
    assert p.items[2].value >= 0
    assert p.items[2].value < 100
    assert p.target == 50

