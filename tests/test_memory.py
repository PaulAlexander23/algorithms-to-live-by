import pytest

from algorithmstolivebypaulalexander.item import Item
from algorithmstolivebypaulalexander.memory import Memory

def test_memory():
    memory = Memory()
    assert memory.items == []

def test_memory_add():
    memory = Memory()
    item = Item("data",unique_id=1)
    memory.add(item)
    assert memory.items == [item]

def test_memory_add_multiple():
    memory = Memory()
    item1 = Item("data1",unique_id=1)
    item2 = Item("data2",unique_id=2)
    memory.add(item1)
    memory.add(item2)
    assert memory.items == [item1, item2]

def test_memory_get():
    memory = Memory()
    item = Item("data",unique_id=1)
    memory.add(item)
    assert memory.get(1) == item

def test_memory_get_not_found():
    memory = Memory()
    item = Item("data", unique_id=1)
    memory.add(item)
    assert memory.get(2) == None

def test_memory_get_multiple():
    memory = Memory()
    item1 = Item("data1",unique_id=1)
    item2 = Item("data2",unique_id=2)
    memory.add(item1)
    memory.add(item2)
    assert memory.get(1) == item1
    assert memory.get(2) == item2
    assert memory.get(3) == None

def test_memory_get_multiple_same_id():
    memory = Memory()
    item1 = Item("data1", unique_id=1)
    item2 = Item("data2", unique_id=1)
    memory.add(item1)
    memory.add(item2)
    assert memory.get(1) == item1

