from typing import List


class BoxBlur:
    @classmethod
    def box_blur(cls, image: List[List[int]]) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        result = []
        for x, row in enumerate(image):
            if x == 0 or x == num_rows - 1:
                continue
            new_row = []
            for y, px in enumerate(row):
                if y == 0 or y == num_cols - 1:
                    continue
                new_row.append(cls._kernel_filter(image, x, y))
            result.append(new_row)
        return result

    @classmethod
    def _kernel_filter(cls, image: List[List[int]], x: int, y: int) -> int:
        cell = image[x][y]
        up = image[x - 1][y]
        up_right = image[x - 1][y + 1]
        right = image[x][y + 1]
        down_right = image[x + 1][y + 1]
        down = image[x + 1][y]
        down_left = image[x + 1][y - 1]
        left = image[x][y - 1]
        up_left = image[x - 1][y - 1]
        sum_val = sum([cell, up, up_right, right, down_right, down, down_left, left, up_left])
        return sum_val // 9
