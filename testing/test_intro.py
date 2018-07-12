import unittest
import palindrome
from palindrome import Palindrome

def fun(num):
    return num

class Palindrome_Test(unittest.TestCase):
    #always name tests test_* and be descriptive of what it does
    def test_fun_returns_8(self):
        self.assertEqual(palindrome.fun(8), 8)

    def test_for_palindrome(self):
        pal = Palindrome()
        self.assertTrue(palindrome.is_palindrome())


if __name__ == '__main__':
    unittest.main()

