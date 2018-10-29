#!/bin/python3

# Hamming code is a linear block code of length 2^r - 1 for some natural number r
# The dimension, k, of a Hamming code is 2^r - 1 - r and contains 2^k codewords

import numpy as np
from Encoder.encoder import number_to_binary_array


def find_r(length):
    r = 0
    j = length + 1
    while j > 1:
        j //= 2
        r += 1
    return r


class HammingDecoder:

    def __init__(self):
        self.length = None
        self.dim = None
        self.H = None

    def decode(self, word):
        if self.length != len(word):
            self.length = len(word)
            r = find_r(self.length)
            self.dim = 2**r - 1 - r
            H = [number_to_binary_array(i, r) for i in reversed(range(1, 2**r))]
            Id_k = [number_to_binary_array(2**i, self.length) for i in reversed(range(self.length))]
            # SDA is 'standard decoding array' where keys are syndromes and values are coset leaders
            self.SDA = dict(zip([tuple(h) for h in H], [tuple(i) for i in Id_k]))
            self.SDA[tuple([0]*r)] = tuple([0]*self.length)
            self.H = np.array(H)
        syndrome = np.array([int(i) for i in word]) @ self.H % 2
        e = self.SDA[tuple(syndrome)]
        return ''.join(str((int(i[0]) + i[1]) % 2) for i in zip(word, e))


if __name__ == '__main__':
    pass
