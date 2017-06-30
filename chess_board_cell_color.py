
def chess_board_cell_color(cell1, cell2):
    if _is_black(cell1) == _is_black(cell2):
        return True
    return False


def _is_black(cell):
    return (ord(cell[0]) % 2 != 0 and int(cell[1]) % 2 != 0) or \
           (ord(cell[0]) % 2 == 0 and int(cell[1]) % 2 == 0)
