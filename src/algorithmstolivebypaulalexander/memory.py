
from algorithmstolivebypaulalexander.item import Item

class Memory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get(self, id):
        for item in self.items:
            if item.unique_id == id:
                return item

        return None
