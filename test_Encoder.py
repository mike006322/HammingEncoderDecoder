import unittest
import Encoder
import numpy as np

class Test(unittest.TestCase):

    def test_number_to_binary_array(self):
        self.assertEqual(Encoder.number_to_binary_array(2, 3), [0, 1, 0])
        self.assertEqual(Encoder.number_to_binary_array(1, 3), [0, 0, 1])

    def test_init(self):
        Hamming7 = Encoder.Hamming_encoder(3)
        H = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(Hamming7.H.all(), H.all())
        self.assertEqual((np.array([0, 0, 0, 0, 0, 0, 0]) @ Hamming7.H).all(), np.array([0, 0, 0]).all())
        G = np.array([[1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1]])
        self.assertEqual(G.all(), Hamming7.G.all())

    def test_encode(self):
        Hamming7 = Encoder.Hamming_encoder(3)
        vector = [1, 0, 1, 0]
        codeword = np.array([1, 0, 1, 0, 0, 1, 0])
        self.assertEqual(Hamming7.encode(vector).all(), codeword.all())
        self.assertEqual(Hamming7.encode(np.array(vector)).all(), codeword.all())


if __name__ == '__main__':
    unittest.main()
