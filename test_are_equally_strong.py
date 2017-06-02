import unittest
from are_equally_strong import AreEquallyStrong


class TestAreEquallyStrong(unittest.TestCase):
    def test_1(self):
        your_left = 10
        your_right = 15
        friends_left = 15
        friends_right = 10
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)

    def test_2(self):
        your_left = 15
        your_right = 10
        friends_left = 15
        friends_right = 10
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)

    def test_3(self):
        your_left = 15
        your_right = 10
        friends_left = 15
        friends_right = 9
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertFalse(result)

    def test_4(self):
        your_left = 10
        your_right = 5
        friends_left = 5
        friends_right = 10
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)

    def test_5(self):
        your_left = 10
        your_right = 15
        friends_left = 5
        friends_right = 20
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertFalse(result)

    def test_6(self):
        your_left = 10
        your_right = 20
        friends_left = 10
        friends_right = 20
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)

    def test_7(self):
        your_left = 5
        your_right = 20
        friends_left = 20
        friends_right = 5
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)

    def test_8(self):
        your_left = 20
        your_right = 15
        friends_left = 5
        friends_right = 20
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertFalse(result)

    def test_9(self):
        your_left = 5
        your_right = 10
        friends_left = 5
        friends_right = 10
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)

    def test_10(self):
        your_left = 1
        your_right = 10
        friends_left = 10
        friends_right = 0
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertFalse(result)

    def test_11(self):
        your_left = 5
        your_right = 5
        friends_left = 10
        friends_right = 10
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertFalse(result)

    def test_12(self):
        your_left = 10
        your_right = 5
        friends_left = 10
        friends_right = 6
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertFalse(result)

    def test_13(self):
        your_left = 1
        your_right = 1
        friends_left = 1
        friends_right = 1
        result = AreEquallyStrong.are_equally_strong(your_left, your_right, friends_left, friends_right)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
