import pygame
import sys

from const import *
from game import Game


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    print(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    print("Mouse button is moving")
                elif event.type == pygame.MOUSEBUTTONUP:
                    print("Mouse button is up")
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
