import unittest
from strings_rearrangement import strings_rearrangement


class TestStringsRearrangement(unittest.TestCase):
    def test_1(self):
        input_array = ["aba", "bbb", "bab"]
        result = strings_rearrangement(input_array)
        self.assertFalse(result)

    def test_2(self):
        input_array = ["ab", "bb", "aa"]
        result = strings_rearrangement(input_array)
        self.assertTrue(result)

    def test_3(self):
        input_array = ["q", "q"]
        result = strings_rearrangement(input_array)
        self.assertFalse(result)

    def test_4(self):
        input_array = ["zzzzab", "zzzzbb", "zzzzaa"]
        result = strings_rearrangement(input_array)
        self.assertTrue(result)

    def test_5(self):
        input_array = ["ab", "ad", "ef", "eg"]
        result = strings_rearrangement(input_array)
        self.assertFalse(result)

    def test_6(self):
        input_array = ["abc", "bef", "bcc", "bec", "bbc", "bdc"]
        result = strings_rearrangement(input_array)
        self.assertTrue(result)

    def test_7(self):
        input_array = ["abc", "abx", "axx", "abc"]
        result = strings_rearrangement(input_array)
        self.assertFalse(result)

    def test_8(self):
        input_array = ["abc", "abx", "axx", "abx", "abc"]
        result = strings_rearrangement(input_array)
        self.assertTrue(result)

    def test_9(self):
        input_array = ["f", "g", "a", "h"]
        result = strings_rearrangement(input_array)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
