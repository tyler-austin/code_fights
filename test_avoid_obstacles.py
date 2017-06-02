import unittest
from avoid_obstacles import AvoidObstacles


class TestAvoidObstacles(unittest.TestCase):
    def test_1(self):
        data = [5, 3, 6, 7, 9]
        solution = 4
        result = AvoidObstacles.avoid_obstacles(data)
        self.assertEqual(result, solution)

    def test_2(self):
        data = [2, 3]
        solution = 4
        result = AvoidObstacles.avoid_obstacles(data)
        self.assertEqual(result, solution)

    def test_3(self):
        data = [1, 4, 10, 6, 2]
        solution = 7
        result = AvoidObstacles.avoid_obstacles(data)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
