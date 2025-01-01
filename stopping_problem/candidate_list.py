#!/usr/bin/python3

import numpy as np
from stopping_problem.candidate import candidate

class candidate_list:
    def __init__(self, N):
        self.length = N
        self.generating_mean = 20 + np.random.rand() * 60
        self.generating_std = 5
        self.candidates = [candidate(np.random.normal(loc=self.generating_mean, scale=self.generating_std)) for i in range(N)]
        self.best = max(self.candidates, key=lambda x: x.quality)
