import unittest
from different_symbols_naive import different_symbols_naive


class TestDifferentSymbolsNaive(unittest.TestCase):
    def test_1(self):
        input_string = 'cabca'
        solution = 3
        result = different_symbols_naive(input_string)
        self.assertEqual(result, solution)

    def test_2(self):
        input_string = 'aba'
        solution = 2
        result = different_symbols_naive(input_string)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
