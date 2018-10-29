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


class HammingEncoder:

    def __init__(self, r):
        self.length = 2**r - 1
        self.dim = 2**r - 1 - r
        self.size = 2**self.dim
        # H is parity check matrix
        H = [number_to_binary_array(i, r) for i in reversed(range(1, 2**r))]
        self.H = np.array(H)
        # G is generator matrix
        G = H[:]
        Id_r = [number_to_binary_array(2**i, r) for i in range(r)]
        for row in Id_r:
            G.remove(row)
        Id_k = [number_to_binary_array(2**i, self.dim) for i in reversed(range(self.dim))]
        Id_k = np.array(Id_k)
        self.G = np.concatenate((Id_k, np.array(G)), axis=1)

    def encode(self, vector):
        if type(vector) == list:
            return np.array(vector) @ self.G % 2
        elif type(vector) == np.ndarray:
            return vector @ self.G % 2


if __name__ == '__main__':
    pass
