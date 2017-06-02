import unittest
from are_similar import AreSimilar


class TestAreSimilar(unittest.TestCase):
    def test_1(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        result = AreSimilar.are_similar(a, b)
        self.assertTrue(result)

    def test_2(self):
        a = [1, 2, 3]
        b = [2, 1, 3]
        result = AreSimilar.are_similar(a, b)
        self.assertTrue(result)

    def test_3(self):
        a = [1, 2, 2]
        b = [2, 1, 1]
        result = AreSimilar.are_similar(a, b)
        self.assertFalse(result)

    def test_4(self):
        a = [1, 1, 4]
        b = [1, 2, 3]
        result = AreSimilar.are_similar(a, b)
        self.assertFalse(result)

    def test_5(self):
        a = [1, 2, 3]
        b = [1, 10, 2]
        result = AreSimilar.are_similar(a, b)
        self.assertFalse(result)

    def test_6(self):
        a = [2, 3, 1]
        b = [1, 3, 2]
        result = AreSimilar.are_similar(a, b)
        self.assertTrue(result)

    def test_7(self):
        a = [2, 3, 9]
        b = [10, 3, 2]
        result = AreSimilar.are_similar(a, b)
        self.assertFalse(result)

    def test_8(self):
        a = [4, 6, 3]
        b = [3, 4, 6]
        result = AreSimilar.are_similar(a, b)
        self.assertFalse(result)

    def test_9(self):
        a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
        b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
        result = AreSimilar.are_similar(a, b)
        self.assertTrue(result)

    def test_10(self):
        a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
        b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
        result = AreSimilar.are_similar(a, b)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
