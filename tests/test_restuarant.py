import pytest
from algorithmstolivebypaulalexander.restuarant import restuarant

def test_restuarant():
    r = restuarant(0.89)
    assert r.win_probability == 0.89

def test_bad_restuarant():
    r = restuarant(0)
    assert r.visit() == 0

def test_good_restuarant():
    r = restuarant(1)
    assert r.visit() == 1



