import pygame

from const import *
from board import Board


class Game:
    def __init__(self):
        self.board = Board()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = "#EAEBC4"
                else:
                    color = "#6D9B4F"

                rect = (col*SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.squares[row][col].piece

                if piece:
                    img = pygame.image.load(piece.image)
                    img_center = col*SQSIZE+SQSIZE//2, row*SQSIZE+SQSIZE//2
                    piece.image_container = img.get_rect(center=img_center)
                    surface.blit(img, piece.image_container)
