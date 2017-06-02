import unittest
from array_maximal_adjacent_difference import ArrayMaximalAdjacentDifference


class TestArrayMaximalAdjacentDifference(unittest.TestCase):
    def test_1(self):
        data = [2, 4, 1, 0]
        solution = 3
        result = ArrayMaximalAdjacentDifference.array_maximal_adjacent_difference(data)
        self.assertEqual(result, solution)

    def test_2(self):
        data = [1, 1, 1, 1]
        solution = 0
        result = ArrayMaximalAdjacentDifference.array_maximal_adjacent_difference(data)
        self.assertEqual(result, solution)

    def test_3(self):
        data = [-1, 4, 10, 3, -2]
        solution = 7
        result = ArrayMaximalAdjacentDifference.array_maximal_adjacent_difference(data)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
