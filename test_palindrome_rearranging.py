import unittest
from palindrome_rearranging import PalindromeRearranging


class TestPalindromeRearranging(unittest.TestCase):
    def test_1(self):
        s = 'aabb'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertTrue(result)

    def test_2(self):
        s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertFalse(result)

    def test_3(self):
        s = 'abbcabb'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertTrue(result)

    def test_4(self):
        s = 'zyyzzzzz'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertTrue(result)

    def test_5(self):
        s = 'z'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertTrue(result)

    def test_6(self):
        s = 'zaa'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertTrue(result)

    def test_7(self):
        s = 'abca'
        result = PalindromeRearranging.palindrome_rearranging(s)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
