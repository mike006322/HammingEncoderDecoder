#!/bin/python3

# Hamming code is a linear block code of length 2^r - 1 for some natural number r
# The dimension, k, of a Hamming code is 2^r - 1 - r and contains 2^k codewords
# implemented as function and then as a class

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


def make_identity_matrix(n):
    """
    input n
    output list of lists, identity matrix I_n
    """
    return [number_to_binary_array(2**i, n) for i in reversed(range(n))]


def hamming_encoder(info):
    """
    input is string, list or numpyarray of 1's and 0's
    output is the input with parity check digits such that it's a Hamming Code word of smallest possible length
    """
    hamming_encoder.length = None
    hamming_encoder.dim = None
    hamming_encoder.H = None
    hamming_encoder.G = None
    r = find_sufficient_r(info)
    if hamming_encoder.length != 2**r - 1:
        hamming_encoder.length = 2**r - 1
        hamming_encoder.dim = 2**r - 1 - r
        # H is parity check matrix
        H = [number_to_binary_array(i, r) for i in range(1, 2**r)]
        hamming_encoder.H = np.array(H)
        # G is generator matrix
        G = H[:]
        Id_r = make_identity_matrix(r)
        for row in Id_r:
            G.remove(row)
        Id_k = make_identity_matrix(hamming_encoder.dim)
        Id_k = np.array(Id_k)
        hamming_encoder.G = np.concatenate((Id_k, np.array(G)), axis=1)

    if type(info) == str:
        if hamming_encoder.dim != len(info):
            while hamming_encoder.dim != len(info):
                info = '0' + info
        res = [int(i) for i in info] @ hamming_encoder.G % 2
        return ''.join(str(i) for i in res)

    if type(info) == list:
        if hamming_encoder.dim != len(info):
            while hamming_encoder.dim != len(info):
                info = [0] + info
        return list(info @ hamming_encoder.G % 2)

    if type(info) == np.ndarray:
        if hamming_encoder.dim != len(info):
            while hamming_encoder.dim != len(info):
                np.append([0], info)
        return info @ hamming_encoder.G % 2


class HammingEncoder:
    """
    Class implementation of hamming_encoder method
    """

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
            H = [number_to_binary_array(i, r) for i in range(1, 2**r)]
            self.H = np.array(H)
            # G is generator matrix
            G = H[:]
            Id_r = make_identity_matrix(r)
            for row in Id_r:
                G.remove(row)
            Id_k = make_identity_matrix(self.dim)
            Id_k = np.array(Id_k)
            self.G = np.concatenate((Id_k, np.array(G)), axis=1)

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
            return list(info @ self.G % 2)

        if type(info) == np.ndarray:
            if self.dim != len(info):
                while self.dim != len(info):
                    np.append([0], info)
            return info @ self.G % 2


if __name__ == '__main__':
    pass
