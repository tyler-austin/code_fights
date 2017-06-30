import unittest
from alphabetic_shift import alphabetic_shift


class TestAlphabeticShift(unittest.TestCase):
    def test_1(self):
        input_string = 'crazy'
        solution = 'dsbaz'
        result = alphabetic_shift(input_string)
        self.assertEqual(result, solution)

    def test_2(self):
        input_string = 'z'
        solution = 'a'
        result = alphabetic_shift(input_string)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
