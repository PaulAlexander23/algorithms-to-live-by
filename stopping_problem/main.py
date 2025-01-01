#!/usr/bin/python3

import sys
import os
import numpy as np

# Add the subfolder to the system path
sys.path.append(os.path.dirname(os.path.relpath("../")))

from stopping_problem.candidate import candidate
from stopping_problem.candidate_list import candidate_list
from stopping_problem.algorithms import random_algorithm, user_select_algorithm, optimal_stopping_algorithm

def main():
    print("Stopping Problem")
    print("Select an algorithm:")
    print("1. Random")
    print("2. User Select")
    print("3. Optimal Stopping")

    algorithm = input("Enter the number of the algorithm: ")

    if algorithm == "1":
        a = random_algorithm()
    elif algorithm == "2":
        a = user_select_algorithm()
    elif algorithm == "3":
        a = optimal_stopping_algorithm()
    else:
        print("Invalid algorithm")

        return 1

    N = int(input("Enter the number of candidates: "))
    c = candidate_list(N)


    print(f"Selected candidate: {a.solve(c.candidates).quality}")

    print(f"Best candidate: {c.best.quality}")

    print("")

    print("Candidates:")

    for i in range(N):
        print(f"{i}: {c.candidates[i].quality}")

    return 0


if __name__ == "__main__":
    main()
