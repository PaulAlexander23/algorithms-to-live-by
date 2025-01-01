#!/usr/bin/python3

import numpy as np
from stopping_problem.candidate import candidate

class algorithm:
    def __init__(self):
        pass

    def solve(self, candidates):
        pass

class random_algorithm(algorithm):
    def __init__(self):
        pass

    def solve(self, candidates):
        return candidates[np.random.randint(len(candidates))]


class user_select_algorithm(algorithm):
    def __init__(self):
        pass

    def solve(self, candidates):
        i = 0
        has_candidate_been_selected = False

        while i < len(candidates):
            print(f"{i}: {candidates[i].quality}")

            if input("Select this candidate? (y/n) ") == "y":
                return candidates[i]
            i += 1

        return candidates[i-1]


class optimal_stopping_algorithm(algorithm):
    def __init__(self):
        pass

    def solve(self, candidates):
        i = 0
        max_so_far = 0
        while i < len(candidates) * 0.37:
            max_so_far = max(max_so_far, candidates[i].quality)
            i += 1

        while i < len(candidates):
            if candidates[i].quality > max_so_far:
                return candidates[i]
            i += 1

        return candidates[i-1]
