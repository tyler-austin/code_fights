import unittest
from extract_each_kth import extract_each_kth


class TestExtractEachKth(unittest.TestCase):
    def test_1(self):
        input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        solution = [1, 2, 4, 5, 7, 8, 10]
        result = extract_each_kth(input_array, k)
        self.assertEqual(result, solution)

    def test_2(self):
        input_array = [1, 1, 1, 1, 1]
        k = 1
        solution = []
        result = extract_each_kth(input_array, k)
        self.assertEqual(result, solution)

    def test_3(self):
        input_array = [1, 2, 1, 2, 1, 2, 1, 2]
        k = 2
        solution = [1, 1, 1, 1]
        result = extract_each_kth(input_array, k)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
