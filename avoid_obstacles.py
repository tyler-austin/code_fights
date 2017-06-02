from typing import List


class AvoidObstacles:
    @classmethod
    def avoid_obstacles(cls, obstacles: List[int]) -> int:
        min_len = 2
        found = False
        while not found:
            if cls._valid_length(obstacles, min_len):
                return min_len
            elif min_len > 40:
                return -1
            else:
                min_len += 1

    @classmethod
    def _valid_length(cls, obstacles: List[int], length: int) -> bool:
        for o in obstacles:
            if o % length == 0:
                return False
        return True
