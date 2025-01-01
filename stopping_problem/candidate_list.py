#!/usr/bin/python3

import numpy as np
from stopping_problem.candidate import candidate

class candidate_list:
    def __init__(self, N):
        self.length = N
        self.candidates = [candidate(np.random.rand()) for i in range(N)]
        self.best = max(self.candidates, key=lambda x: x.quality)
