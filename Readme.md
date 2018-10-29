# Hamming Encoder and Decoder

An encoder and decoder for Hamming family of error-correcting
linear block codes.

The encoder takes input and produces a Hamming codeword of a certain
length.

The decoder takes a codeword, corrects it and removes redundant digits.

*Unfinished!* - Still need to make generator matrix of encoder into
 RREF so that it adds redundancy digits to the end of the word.
 Currently it produces hamming codewords with an unspecified generator.

