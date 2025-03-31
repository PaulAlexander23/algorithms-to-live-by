import pytest

from algorithmstolivebypaulalexander.item import Item

def test_item_unique_id():
    apple = Item()
    banana = Item()
    assert (apple.unique_id != banana.unique_id)

def test_item():
    apple = Item("apple", 1)
    assert apple.name == "apple"
    assert apple.value == 1

def test_optional_id():
    apple = Item(name="apple")
    assert apple.unique_id == id(apple)
    assert apple.name == "apple"
    assert apple.value == 0


