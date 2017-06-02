from typing import List


class Minesweeper:
    @classmethod
    def minesweeper(cls, matrix: List[List[bool]]) -> List[List[int]]:
        result = []
        for x, row in enumerate(matrix):
            new_row = []
            for y, col in enumerate(row):
                num_mines = cls._num_neighbor_mines(matrix, x, y)
                new_row.append(num_mines)
            result.append(new_row)
        return result

    @classmethod
    def _num_neighbor_mines(cls, matrix: List[List[bool]], x: int, y: int) -> int:
        up = cls._is_mine(matrix, x - 1, y)
        up_right = cls._is_mine(matrix, x - 1, y + 1)
        right = cls._is_mine(matrix, x, y + 1)
        down_right = cls._is_mine(matrix, x + 1, y + 1)
        down = cls._is_mine(matrix, x + 1, y)
        down_left = cls._is_mine(matrix, x + 1, y - 1)
        left = cls._is_mine(matrix, x, y - 1)
        up_left = cls._is_mine(matrix, x - 1, y - 1)
        mines = sum([up, up_right, right, down_right, down, down_left, left, up_left])
        return mines

    @classmethod
    def _is_mine(cls, matrix: List[List[bool]], x: int, y: int) -> bool:
        try:
            if x >= 0 and y >= 0:
                return matrix[x][y]
            else:
                return False
        except IndexError:
            return False
