#!/usr/bin/python3

import argparse

import numpy as np
import scipy as sp

def main():
    parser = argparse.ArgumentParser(description=
            'Attempt to solve the optimal stopping problem.')
    parser.add_argument('N',help='Number of candidates')
    parser.add_argument('--37-Rule',help='use the 37% rule.')

    args = parser.parse_args()





if __name__ == "__main__":
    main()
