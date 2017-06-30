import unittest
from absolute_values_sum_minimization import absolute_values_sum_minimization


class TestAbsoluteValuesSumMinimization(unittest.TestCase):
    def test_1(self):
        a = [2, 4, 7]
        solution = 4
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

    def test_2(self):
        a = [1, 1, 3, 4]
        solution = 1
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

    def test_3(self):
        a = [23]
        solution = 23
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

    def test_4(self):
        a = [-10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4, -3, -2, -1,
             0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
             19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
             38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        solution = 15
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

    def test_5(self):
        a = [-4, -1]
        solution = -4
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

    def test_6(self):
        a = [0, 7, 9]
        solution = 7
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

    def test_7(self):
        a = [-1000000, -10000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000]
        solution = 0
        result = absolute_values_sum_minimization(a)
        self.assertEqual(result, solution)

if __name__ == '__main__':
    unittest.main()
