#!usr/bin/python3

import numpy as np
import scipy as sp

def main(N):
    list1 = sp.norm.rvs(size=N)

    i = 0
    m = -3
    while i < 0.37*N:
        m = max(m,list1[i])

    while i < N:
        if list1[i] > m:
            x = list1[i]

    best-x = max(list1)
    return x
