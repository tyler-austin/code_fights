import unittest
from random import randint
from array_max_consecutive_sum import array_max_consecutive_sum


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_array = [2, 3, 5, 1, 6]
        k = 2
        solution = 8
        result = array_max_consecutive_sum(input_array, k)
        self.assertEqual(result, solution)

    def test_2(self):
        input_array = [2, 4, 10, 1]
        k = 2
        solution = 14
        result = array_max_consecutive_sum(input_array, k)
        self.assertEqual(result, solution)

    def test_3(self):
        input_array = [1, 3, 2, 4]
        k = 3
        solution = 9
        result = array_max_consecutive_sum(input_array, k)
        self.assertEqual(result, solution)

    def test_4(self):
        input_array = [3, 2, 1, 1]
        k = 1
        solution = 3
        result = array_max_consecutive_sum(input_array, k)
        self.assertEqual(result, solution)

    # def test_5(self):
    #     input_array = [randint(1, 1000) for i in range(0, 10**5, 1)]
    #     k = randint(1, 10**5)
    #     solution = 3
    #     result = array_max_consecutive_sum(input_array, k)
    #     self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
