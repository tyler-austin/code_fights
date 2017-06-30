import unittest
from circle_of_numbers import circle_of_numbers


class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 10
        first_number = 2
        solution = 7
        result = circle_of_numbers(n, first_number)
        self.assertEqual(result, solution)

    def test_2(self):
        n = 10
        first_number = 7
        solution = 2
        result = circle_of_numbers(n, first_number)
        self.assertEqual(result, solution)

    def test_3(self):
        n = 4
        first_number = 1
        solution = 3
        result = circle_of_numbers(n, first_number)
        self.assertEqual(result, solution)

    def test_4(self):
        n = 6
        first_number = 3
        solution = 0
        result = circle_of_numbers(n, first_number)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
