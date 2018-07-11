import unittest

def fun(num):
    return num

class My_Test(unittest.TestCase):
    #always name tests test_* and be descriptive of what it does
    def test_fun_returns_8(self):
        self.assertEqual(fun(8), 8)

if __name__ == '__main__':
    unittest.main()

