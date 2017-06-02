from typing import List
from copy import deepcopy


class AreSimilar:
    @classmethod
    def are_similar(cls, a: List[int], b: List[int]):
        if a == b:
            return True
        elif cls._single_swap(a, b):
            return True
        else:
            return False

    @classmethod
    def _same_digits(cls, a: List[int], b: List[int]):
        x, y = deepcopy(a), deepcopy(b)
        x.sort()
        y.sort()
        return x == y

    @classmethod
    def _single_swap(cls, a: List[int], b: List[int]):
        if not cls._same_digits(a, b):
            return False
        differences = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                differences += 1
            if differences > 2:
                break
        return differences <= 2
