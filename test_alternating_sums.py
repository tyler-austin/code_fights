import unittest
from alternating_sums import AlternatingSums


class TestAlternatingSums(unittest.TestCase):
    def test_1(self):
        a = [50, 60, 60, 45, 70]
        solution = [180, 105]
        result = AlternatingSums.alternating_sums(a)
        self.assertEqual(result, solution)

    def test_2(self):
        a = [100, 50]
        solution = [100, 50]
        result = AlternatingSums.alternating_sums(a)
        self.assertEqual(result, solution)

    def test_3(self):
        a = [80]
        solution = [80, 0]
        result = AlternatingSums.alternating_sums(a)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
