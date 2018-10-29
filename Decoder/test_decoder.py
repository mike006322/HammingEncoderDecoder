import unittest
from Decoder import decoder


class Test(unittest.TestCase):

    def test_find_r(self):
        self.assertEqual(decoder.find_r(7), 3)

    def test_decode(self):
        d = decoder.HammingDecoder()
        # self.assertEqual(d.decode('1010100'), '1010101')
        # self.assertEqual(d.decode('1010101'), '1010101')
        # self.assertEqual(d.decode('010'), '000')
        # self.assertEqual(d.decode('000'), '000')
        print(d.decode('0000000'))


if __name__ == '__main__':
    unittest.main()
