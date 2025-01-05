import pytest

from sorting.item import item

def test_item():
    apple = item("apple", 1)
    assert apple.name == "apple"
    assert apple.value == 1
