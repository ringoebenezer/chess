import os


class Piece:
    def __init__(self, name, color, value, image=None, image_container=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.image = image
        self.valid_moves = []
        self.moved = False
        self.set_image()
        self.image_container = image_container

    def set_image(self, size=80):
        self.image = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_moves(self, move):
        self.valid_moves.append(move)


class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.0)


class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 100000.0)
