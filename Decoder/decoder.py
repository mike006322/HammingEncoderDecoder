#!/bin/python3

# Hamming code is a linear block code of length 2^r - 1 for some natural number r
# The dimension, k, of a Hamming code is 2^r - 1 - r and contains 2^k codewords
# implemented as function and then as a class

import numpy as np
from Encoder.encoder import number_to_binary_array
from Encoder.encoder import make_identity_matrix


def find_r(length):
    r = 0
    j = length + 1
    while j > 1:
        j //= 2
        r += 1
    return r


def hamming_decoder(word):
    """
    input is a codeword from a Hamming family of codes
    codeword is first corrected
    then the parity check bits are removed
    """
    hamming_decoder.length = None
    hamming_decoder.dim = None
    hamming_decoder.H = None
    hamming_decoder.G = None
    hamming_decoder.SDA = None
    if hamming_decoder.length != len(word):
        hamming_decoder.length = len(word)
        r = find_r(hamming_decoder.length)
        hamming_decoder.dim = 2**r - 1 - r
        H = [number_to_binary_array(i, r) for i in range(1, 2**r)]
        Id_k = make_identity_matrix(hamming_decoder.length)
        # SDA is 'standard decoding array' where keys are syndromes and values are coset leaders
        hamming_decoder.SDA = dict(zip([tuple(h) for h in H], [tuple(i) for i in Id_k]))
        hamming_decoder.SDA[tuple([0]*r)] = tuple([0]*hamming_decoder.length)
        hamming_decoder.H = np.array(H)
    syndrome = np.array([int(i) for i in word]) @ hamming_decoder.H % 2
    e = hamming_decoder.SDA[tuple(syndrome)]
    sent_word = [(int(i[0]) + i[1]) % 2 for i in zip(word, e)]
    info = [int(i) for i in sent_word][:hamming_decoder.dim]
    return ''.join(str(int(i)) for i in info)


class HammingDecoder:
    """
    Class implementation of hamming_decoder method
    """

    def __init__(self):
        self.length = None
        self.dim = None
        self.H = None
        self.SDA = None

    def decode(self, word):
        if self.length != len(word):
            self.length = len(word)
            r = find_r(self.length)
            self.dim = 2**r - 1 - r
            H = [number_to_binary_array(i, r) for i in range(1, 2**r)]
            Id_k = make_identity_matrix(self.length)
            # SDA is 'standard decoding array' where keys are syndromes and values are coset leaders
            self.SDA = dict(zip([tuple(h) for h in H], [tuple(i) for i in Id_k]))
            self.SDA[tuple([0]*r)] = tuple([0]*self.length)
            self.H = np.array(H)
        syndrome = np.array([int(i) for i in word]) @ self.H % 2
        e = self.SDA[tuple(syndrome)]
        sent_word = [(int(i[0]) + i[1]) % 2 for i in zip(word, e)]
        info = [int(i) for i in sent_word][:self.dim]
        return ''.join(str(int(i)) for i in info)


if __name__ == '__main__':
    pass
