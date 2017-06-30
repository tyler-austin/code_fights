import unittest
from chess_board_cell_color import chess_board_cell_color


class TestChessBoardCellColor(unittest.TestCase):
    def test_1(self):
        cell1 = 'A1'
        cell2 = 'C3'
        result = chess_board_cell_color(cell1, cell2)
        self.assertTrue(result)

    def test_2(self):
        cell1 = 'A1'
        cell2 = 'H3'
        result = chess_board_cell_color(cell1, cell2)
        self.assertFalse(result)

    def test_3(self):
        cell1 = 'A1'
        cell2 = 'A2'
        result = chess_board_cell_color(cell1, cell2)
        self.assertFalse(result)

    def test_4(self):
        cell1 = 'A1'
        cell2 = 'B2'
        result = chess_board_cell_color(cell1, cell2)
        self.assertTrue(result)

    def test_5(self):
        cell1 = 'B3'
        cell2 = 'H8'
        result = chess_board_cell_color(cell1, cell2)
        self.assertFalse(result)

    def test_6(self):
        cell1 = 'C3'
        cell2 = 'B5'
        result = chess_board_cell_color(cell1, cell2)
        self.assertFalse(result)

    def test_7(self):
        cell1 = 'G5'
        cell2 = 'E7'
        result = chess_board_cell_color(cell1, cell2)
        self.assertTrue(result)

    def test_8(self):
        cell1 = 'C8'
        cell2 = 'H8'
        result = chess_board_cell_color(cell1, cell2)
        self.assertFalse(result)

    def test_9(self):
        cell1 = 'D2'
        cell2 = 'D2'
        result = chess_board_cell_color(cell1, cell2)
        self.assertTrue(result)

    def test_10(self):
        cell1 = 'A2'
        cell2 = 'A5'
        result = chess_board_cell_color(cell1, cell2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
