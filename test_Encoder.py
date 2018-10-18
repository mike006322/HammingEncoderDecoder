import unittest
import Encoder
import numpy as np

class Test(unittest.TestCase):

    def test_number_to_binary_array(self):
        self.assertEqual(Encoder.number_to_binary_array(2, 3), [0, 1, 0])

    def test_init(self):
        Hamming7 = Encoder.Hamming_encoder(3)
        self.assertEqual(Hamming7.H.all(), np.array([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1]]).all())
        self.assertEqual((np.array([0, 0, 0, 0, 0, 0, 0]) @ Hamming7.H).all(), np.array([0, 0, 0]).all())


if __name__ == '__main__':
    unittest.main()
