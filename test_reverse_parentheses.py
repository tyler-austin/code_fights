import unittest
from reverse_parentheses import ReverseParentheses


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = 'a(bc)de'
        solution = 'acbde'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)

    def test_2(self):
        s = 'a(bcdefghijkl(mno)p)q'
        solution = 'apmnolkjihgfedcbq'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)

    def test_3(self):
        s = 'co(de(fight)s)'
        solution = 'cosfighted'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)

    def test_4(self):
        s = 'Code(Cha(lle)nge)'
        solution = 'CodeegnlleahC'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)

    def test_5(self):
        s = 'Where are the parentheses?'
        solution = 'Where are the parentheses?'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)

    def test_6(self):
        s = 'abc(cba)ab(bac)c'
        solution = 'abcabcabcabc'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)

    def test_7(self):
        s = 'The ((quick (brown) (fox) jumps over the lazy) dog)'
        solution = 'The god quick nworb xof jumps over the lazy'
        result = ReverseParentheses.reverse_parentheses(s)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
