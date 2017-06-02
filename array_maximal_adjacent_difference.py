from typing import List


class ArrayMaximalAdjacentDifference:
    @classmethod
    def array_maximal_adjacent_difference(cls, data: List[int]):
        max_abs_dif = 0
        prev = data[0]
        for d in data:
            abs_dif = abs(d - prev)
            if abs_dif > max_abs_dif:
                max_abs_dif = abs_dif
            prev = d
        return max_abs_dif
