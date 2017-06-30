import unittest
from deposit_profit import deposit_profit


class TestDepositProfit(unittest.TestCase):
    def test_1(self):
        deposit = 100
        rate = 20
        threshold = 170
        solution = 3
        result = deposit_profit(deposit, rate, threshold)
        self.assertEqual(result, solution)

    def test_2(self):
        deposit = 100
        rate = 1
        threshold = 101
        solution = 1
        result = deposit_profit(deposit, rate, threshold)
        self.assertEqual(result, solution)

    def test_3(self):
        deposit = 1
        rate = 100
        threshold = 64
        solution = 6
        result = deposit_profit(deposit, rate, threshold)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
