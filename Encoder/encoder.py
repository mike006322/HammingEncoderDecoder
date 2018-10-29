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


def find_sufficient_r(word):
    """
    returns r such that dimension of the Hamming code will be enough to encode the word
    """
    r = 1
    while 2**r - 1 - r < len(word):
        r += 1
    return r


class HammingEncoder:

    def __init__(self):
        self.length = None
        self.dim = None
        self.H = None
        self.G = None

    def encode(self, info):
        r = find_sufficient_r(info)
        if self.length != 2**r - 1:
            self.length = 2**r - 1
            self.dim = 2**r - 1 - r
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
            # self.G = np.array(rref(list(self.G)))

        if type(info) == str:
            if self.dim != len(info):
                while self.dim != len(info):
                    info = '0' + info
            res = [int(i) for i in info] @ self.G % 2
            return ''.join(str(i) for i in res)

        if type(info) == list:
            if self.dim != len(info):
                while self.dim != len(info):
                    info = [0] + info
            res = info @ self.G % 2
            return ''.join(str(i) for i in res)

        if type(info) == np.ndarray:
            if self.dim != len(info):
                while self.dim != len(info):
                    np.append([0], info)
            res = info @ self.G % 2
            return ''.join(str(i) for i in res)


if __name__ == '__main__':
    pass
