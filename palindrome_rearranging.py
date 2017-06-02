
class PalindromeRearranging:
    @classmethod
    def palindrome_rearranging(cls, data: str):
        unique = set(data)
        num_odd_occur = 0
        for c in unique:
            if data.count(c) % 2 != 0:
                num_odd_occur += 1
            if num_odd_occur > 1:
                return False
        return True
