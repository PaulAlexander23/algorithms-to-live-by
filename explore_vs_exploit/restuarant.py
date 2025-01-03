#!/usr/bin/python3

import numpy as np

class restuarant:
    def __init__(self, win_probability):
        self.win_probability = win_probability

    def visit(self):
        return np.random.rand() < self.win_probability
