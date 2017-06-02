from typing import List


class ArrayChange:
    @classmethod
    def array_change(cls, data: List[int]):
        increments = 0
        prev = data[0] - 1
        for d in data:
            if prev - d >= 0:
                increment = prev - d + 1
                increments += increment
                d += increment
            prev = d
        return increments
