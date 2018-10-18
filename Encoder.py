#!/bin/python3

# Hamming code is a linear block code of length 2^r - 1 for some natural number r
# The dimension, k, of a Hamming code is 2^r - 1 - r and contains 2^k codewords

import numpy as np

def number_to_binary_array(n, r):
    """
    input integer
    output binary representation of integer as values in an array that can hold numbers less than 2^r
    """
    res = [int(i) for i in bin(n)[2:]]
    while len(res) < r:
        res = [0] + res
    return res

class Hamming_encoder():

    def __init__(self, r):
        self.length = 2**r - 1
        self.dim = 2**r - 1 - r
        self.size = 2**self.dim
        # H is parity check matrix
        H = [number_to_binary_array(i, r) for i in range(2**r - 1, 0, -1)]
        self.H = np.array(H)
        # G is generator matrix
        G = []
        self.G = np.array(G)

if __name__ == '__main__':
    pass
