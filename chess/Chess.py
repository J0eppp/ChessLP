from .Board import Board
from .Pieces import Piece


class Chess:
    def __init__(self):
        self.board = Board()

    def move(self, p1: int, p2: int):
        pass

    def check_pawn_promotion(self):
        for i in range(8):
            if not self.turn and self.board.board[0][i] != None and self.board.board[0][i].name == 'P':
                self.promotion(0, i)
            elif self.turn and self.board.board[7][i] != None and self.board.board[7][i].name == 'P':
                self.promotion(7, i)
