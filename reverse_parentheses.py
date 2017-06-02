import re


class ReverseParentheses:
    @classmethod
    def reverse_parentheses(cls, input_str: str):
        if '(' in input_str:
            return cls.reverse_parentheses(cls._reverse_substring(input_str))
        else:
            return input_str

    @classmethod
    def _reverse_substring(cls, input_str: str) -> str:
        pattern = r"\(([^()]*)\)"
        regexp = re.compile(pattern)
        substr = regexp.search(input_str)
        substr_list = list(substr.group())
        substr_list = [c for c in substr_list if c not in '()']
        substr_list.reverse()
        substr = ''.join(substr_list)
        return re.sub(pattern, substr, input_str, count=1)
