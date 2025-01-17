import unittest

import math_utils

class MahtUtilTest(unittest.TestCase):
    def test_add(self):
        a = 2
        b = 3
        expected = 5
        actual = math_utils.add(a, b)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()