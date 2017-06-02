import unittest
from minesweeper import Minesweeper


class TestMinesweeper(unittest.TestCase):
    def test_1(self):
        matrix = [[True,  False, False],
                  [False, True,  False],
                  [False, False, False]]
        solution = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
        result = Minesweeper.minesweeper(matrix)
        self.assertEqual(result, solution)

    def test_2(self):
        matrix = [[False, False, False],
                  [False, False, False]]
        solution = [[0, 0, 0],
                    [0, 0, 0]]
        result = Minesweeper.minesweeper(matrix)
        self.assertEqual(result, solution)

    def test_3(self):
        matrix = [[True,  False, False,  True],
                  [False, False,  True, False],
                  [True,   True, False,  True]]
        solution = [[0, 2, 2, 1],
                    [3, 4, 3, 3],
                    [1, 2, 3, 1]]
        result = Minesweeper.minesweeper(matrix)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
