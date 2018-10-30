import unittest
from Decoder import decoder
from Decoder.decoder import hamming_decoder


class Test(unittest.TestCase):

    def test_find_r(self):
        self.assertEqual(decoder.find_r(7), 3)

    def test_decode(self):
        d = decoder.HammingDecoder()
        self.assertEqual(d.decode('010'), '0')
        self.assertEqual(d.decode('000'), '0')
        self.assertEqual(d.decode('0000000'), '0000')
        self.assertEqual(d.decode('000001010101000'), '00000101010')

    def test_hamming_decoder(self):
        self.assertEqual(hamming_decoder('000001010101000'), '00000101010')


if __name__ == '__main__':
    unittest.main()
