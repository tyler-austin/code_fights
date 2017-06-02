import unittest
from is_IPv4_address import IsIPv4Address


class TestIsIPv4Address(unittest.TestCase):
    def test_1(self):
        s = '172.16.254.1'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertTrue(result)

    def test_2(self):
        s = '172.316.254.1'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_3(self):
        s = '.254.255.0'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_4(self):
        s = '1.1.1.1a'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_5(self):
        s = '0.254.255.0'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertTrue(result)

    def test_6(self):
        s = '0..1.0'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_7(self):
        s = '1.1.1.1.1'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_8(self):
        s = '1.256.1.1'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_9(self):
        s = 'a0.1.1.1'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

    def test_10(self):
        s = '0.1.1.256'
        result = IsIPv4Address.is_IPv4_address(s)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
