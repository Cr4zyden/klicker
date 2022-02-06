import pygame
from pygame.color import THECOLORS

class Shop:
    def __init__(self,screen,balance):
        self.balance = balance
        self.screen = screen
        self.image = pygame.image.load('img/shop.png')
        self.banance_image = pygame.image.load('img/balance.png')


