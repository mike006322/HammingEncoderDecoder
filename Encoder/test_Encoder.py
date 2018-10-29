import unittest
from Encoder import encoder
import numpy as np


class Test(unittest.TestCase):

    def test_number_to_binary_array(self):
        self.assertEqual(encoder.number_to_binary_array(2, 3), [0, 1, 0])
        self.assertEqual(encoder.number_to_binary_array(1, 3), [0, 0, 1])

    def test_find_sufficient_r(self):
        self.assertEqual(encoder.find_sufficient_r('0101'), 3)
        self.assertEqual(encoder.find_sufficient_r('01010'), 4)
        self.assertEqual(encoder.find_sufficient_r('01010101010'), 4)
        self.assertEqual(encoder.find_sufficient_r('010101010101'), 5)

    def test_encode(self):
        e = encoder.HammingEncoder()
        self.assertEqual(e.encode('0000'), '0000000')
        H = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(e.H.all(), H.all())
        self.assertEqual((np.array([0, 0, 0, 0, 0, 0, 0]) @ e.H).all(), np.array([0, 0, 0]).all())
        G = np.array([[1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1]])
        self.assertEqual(G.all(), e.G.all())
        vector = [1, 0, 1, 0]
        codeword = '1010010'
        self.assertEqual(e.encode(vector), codeword)
        self.assertEqual(e.encode(np.array(vector)), codeword)
        print(e.encode(vector))


if __name__ == '__main__':
    unittest.main()
