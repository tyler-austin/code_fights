import unittest
from box_blur import BoxBlur


class TestBoxBlur(unittest.TestCase):
    def test_1(self):
        image = [[1, 1, 1],
                 [1, 7, 1],
                 [1, 1, 1]]
        solution = [[1]]
        result = BoxBlur.box_blur(image)
        self.assertEqual(result, solution)

    def test_2(self):
        image = [[0,  18,  9],
                 [27,  9,  0],
                 [81, 63, 45]]
        solution = [[28]]
        result = BoxBlur.box_blur(image)
        self.assertEqual(result, solution)

    def test_3(self):
        image = [[36,  0, 18,  9],
                 [27, 54,  9,  0],
                 [81, 63, 72, 45]]
        solution = [[40, 30]]
        result = BoxBlur.box_blur(image)
        self.assertEqual(result, solution)

    def test_4(self):
        image = [[7,  4,  0,  1],
                 [5,  6,  2,  2],
                 [6, 10,  7,  8],
                 [1,  4,  2,  0]]
        solution = [[5, 4],
                    [4, 4]]
        result = BoxBlur.box_blur(image)
        self.assertEqual(result, solution)

    def test_5(self):
        image = [[36,  0, 18,  9,  9, 45, 27],
                 [27,  0, 54,  9,  0, 63, 90],
                 [81, 63, 72, 45, 18, 27,  0],
                 [0,   0,  9, 81, 27, 18, 45],
                 [45, 45, 27, 27, 90, 81, 72],
                 [45, 18,  9,  0,  9, 18, 45],
                 [27, 81, 36, 63, 63, 72, 81]]
        solution = [[39, 30, 26, 25, 31],
                    [34, 37, 35, 32, 32],
                    [38, 41, 44, 46, 42],
                    [22, 24, 31, 39, 45],
                    [37, 34, 36, 47, 59]]
        result = BoxBlur.box_blur(image)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
