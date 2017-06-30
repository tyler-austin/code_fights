import unittest
from first_digit import first_digit


class TestFirstDigit(unittest.TestCase):
    def test_1(self):
        input_string = 'var_1__Int'
        solution = '1'
        result = first_digit(input_string)
        self.assertEqual(result, solution)

    def test_2(self):
        input_string = 'q2q-q'
        solution = '2'
        result = first_digit(input_string)
        self.assertEqual(result, solution)

    def test_3(self):
        input_string = '0ss'
        solution = '0'
        result = first_digit(input_string)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
