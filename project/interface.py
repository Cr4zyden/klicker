import pygame

from interface_buttons.seed import Seed
from interface_buttons.name import Name
from interface_buttons.level import Level
from interface_buttons.shop_button import ShopButton

class Interface:
    def __init__(self):
        self.seed = Seed()
        self.name = Name()
        self.level = Level()
        self.shop_button = ShopButton()
    def draw(self,screen):
        self.shop_button.draw(screen)
        self.seed.draw(screen)
        self.name.draw(screen)
        self.level.draw(screen)
    def draw_healt_bar(self,screen):
        rect = pygame.Rect(100,60,300,50)
        pygame.draw.rect(screen, (255, 0, 0), rect, 0)
