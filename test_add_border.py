import unittest
from add_border import AddBorder


class TestAddBorder(unittest.TestCase):
    def test_1(self):
        picture = ["abc",
                   "ded"]
        solution = ["*****",
                    "*abc*",
                    "*ded*",
                    "*****"]
        result = AddBorder.add_border(picture)
        self.assertEqual(result, solution)

    def test_2(self):
        picture = ["a"]
        solution = ["***",
                    "*a*",
                    "***"]
        result = AddBorder.add_border(picture)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
