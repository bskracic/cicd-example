import unittest

import math_utils
import word_utils

class MahtUtilTest(unittest.TestCase):
    def test_add(self):
        a = 2
        b = 3
        expected = 5
        actual = math_utils.add(a, b)
        self.assertEqual(actual, expected)

class WordUtilsTest(unittest.TestCase):
    def test_get_ith_letter(self):
        word = "Something"
        index = 2
        expected = "m"
        actual = word_utils.get_ith_letter(word, index)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()