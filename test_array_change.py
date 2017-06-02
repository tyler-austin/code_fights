import unittest
from array_change import ArrayChange


class TestArrayChange(unittest.TestCase):
    def test_1(self):
        input_array = [1, 1, 1]
        solution = 3
        result = ArrayChange.array_change(input_array)
        self.assertEqual(result, solution)

    def test_2(self):
        input_array = [-1000, 0, -2, 0]
        solution = 5
        result = ArrayChange.array_change(input_array)
        self.assertEqual(result, solution)

    def test_3(self):
        input_array = [2, 1, 10, 1]
        solution = 12
        result = ArrayChange.array_change(input_array)
        self.assertEqual(result, solution)

    def test_4(self):
        input_array = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
        solution = 13
        result = ArrayChange.array_change(input_array)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
