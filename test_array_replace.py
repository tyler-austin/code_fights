import unittest
from array_replace import ArrayReplace


class TestArrayReplace(unittest.TestCase):
    def test_1(self):
        input_array = [1, 2, 1]
        elem_to_replace = 1
        substitution_elem = 3
        solution = [3, 2, 3]
        result = ArrayReplace.array_replace(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(result, solution)

    def test_2(self):
        input_array = [1, 2, 3, 4, 5]
        elem_to_replace = 3
        substitution_elem = 0
        solution = [1, 2, 0, 4, 5]
        result = ArrayReplace.array_replace(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(result, solution)

    def test_3(self):
        input_array = [1, 1, 1]
        elem_to_replace = 1
        substitution_elem = 10
        solution = [10, 10, 10]
        result = ArrayReplace.array_replace(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
