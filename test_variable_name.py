import unittest
from variable_name import variable_name


class TestVariableName(unittest.TestCase):
    def test_1(self):
        name = 'var_1__Int'
        result = variable_name(name)
        self.assertTrue(result)

    def test_2(self):
        name = 'qq-q'
        result = variable_name(name)
        self.assertFalse(result)

    def test_3(self):
        name = '2w2'
        result = variable_name(name)
        self.assertFalse(result)

    def test_4(self):
        name = ' variable'
        result = variable_name(name)
        self.assertFalse(result)

    def test_5(self):
        name = 'va[riable0'
        result = variable_name(name)
        self.assertFalse(result)

    def test_6(self):
        name = 'variable0'
        result = variable_name(name)
        self.assertTrue(result)

    def test_7(self):
        name = 'a'
        result = variable_name(name)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
