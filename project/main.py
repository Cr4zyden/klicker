import pygame

from interface import Interface
from shop import Shop


class Main():
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.interface = Interface()
        self.shop = Shop(self.screen,0)
    def start(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                self.shop.start(event)
    def draw(self):
        self.interface.draw(self.screen)
        pygame.display.update()

main = Main()
main.start()