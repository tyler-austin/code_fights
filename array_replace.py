from typing import List


class ArrayReplace:
    @classmethod
    def array_replace(cls, input_array: List[int], elem_to_replace: int, substitution_elem: int) -> List[int]:
        return [substitution_elem if d == elem_to_replace else d for d in input_array]
