class Piece:
    def __init__(self):
        pass

    def is_valid_move(self) -> bool:
        return False

    def is_white(self) -> bool:
        pass

    def __str__(self) -> str:
        return ''


class Pawn(Piece):
    def __init__(self):
        super().__init__()


class GhostPawn(Piece):
    """
    A pseudo pawn that can be used when en passent is possible
    """


class Knight(Piece):
    def __init__(self):
        super().__init__()


class Bishop(Piece):
    def __init__(self):
        super().__init__()


class Rook(Piece):
    def __init__(self):
        super().__init__()


class Queen(Piece):
    def __init__(self):
        super().__init__()


class King(Piece):
    def __init__(self):
        super().__init__()

    def can_castle(self) -> bool:
        pass
