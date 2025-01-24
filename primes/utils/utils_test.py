import unittest
import utils

class TestNumberToBinaryString(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(utils.generateBinary(0),   "00000000000000000000000000000000", "Binary of 0 should be 32 zeros")
        self.assertEqual(utils.generateBinary(1),   "00000000000000000000000000000001", "Binary of 1 should be padded to 32 bits")
        self.assertEqual(utils.generateBinary(10),  "00000000000000000000000000001010", "Binary of 10 should be padded to 32 bits")
        self.assertEqual(utils.generateBinary(255), "00000000000000000000000011111111", "Binary of 255 should be padded to 32 bits")

    def test_large_number(self):
        self.assertEqual(utils.generateBinary(1024), "00000000000000000000010000000000", "Binary of 1024 should be padded to 32 bits")

    def test_negative_number(self):
        with self.assertRaises(ValueError, msg="Should raise ValueError for negative numbers"):
            utils.generateBinary(-5)

    def test_edge_cases(self):
        self.assertEqual(utils.generateBinary(2**10),     "00000000000000000000010000000000", "Binary of 2^10 should match 32-bit representation")
        self.assertEqual(utils.generateBinary(2**31 - 1), "01111111111111111111111111111111", "Binary of 2^31-1 should match 32-bit representation")
        self.assertEqual(utils.generateBinary(2**31),     "10000000000000000000000000000000", "Binary of 2^31 should match 32-bit representation")

if __name__ == "__main__":
    unittest.main()
