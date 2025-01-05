import numpy as np

from sorting.item import item

class sorting_problem:
    def __init__(self, N):
        self.N = N
        self.items = []

        for i in range(N):
            self.items.append(item(str(i), np.random.randint(0, 100)))

class searching_problem:
    def __init__(self, N, target):
        self.N = N
        self.items = []
        self.target = target

        for i in range(N):
            self.items.append(item(str(i), np.random.randint(0, 100)))
