import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(caesar_cipher("abc", 3, "encode"), "def")

    def test_decode(self):
        self.assertEqual(caesar_cipher("def", 3, "decode"), "abc")

if __name__ == '__main__':
    unittest.main()

