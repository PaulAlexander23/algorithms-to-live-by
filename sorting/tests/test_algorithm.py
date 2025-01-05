import pytest

from sorting.problem import sorting_problem, searching_problem
from sorting.algorithm import bubble_sort, bubble_sort_search, linear_search

def test_bubble_sort():
    p = sorting_problem(3)
    p.items[0].value = 3
    p.items[1].value = 2
    p.items[2].value = 1

    a = bubble_sort()
    result = a.solve(p)

    assert result[0].value == 1
    assert result[1].value == 2
    assert result[2].value == 3

def test_linear_search_true():
    p = searching_problem(3,3)
    p.items[0].value = 3
    p.items[1].value = 2
    p.items[2].value = 1

    a = linear_search()
    result = a.solve(p)

    assert result == 1

def test_linear_search_false():
    p = searching_problem(3,4)
    p.items[0].value = 3
    p.items[1].value = 2
    p.items[2].value = 1

    a = linear_search()
    result = a.solve(p)

    assert result == 0

def test_bubble_sort_search_true():
    p = searching_problem(3,3)
    p.items[0].value = 3
    p.items[1].value = 2
    p.items[2].value = 1

    a = bubble_sort_search()
    result = a.solve(p)

    assert result == 1

def test_bubble_sort_search_false():
    p = searching_problem(3,4)
    p.items[0].value = 3
    p.items[1].value = 2
    p.items[2].value = 1

    a = bubble_sort_search()
    result = a.solve(p)

    assert result == 0
