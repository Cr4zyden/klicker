import pygame
from pygame.color import THECOLORS

class Shop:
    def __init__(self,screen,balance):
        self.balance = balance
        self.screen = screen
        self.image = pygame.image.load('img/shop.png')
        self.banance_image = pygame.image.load('img/balance.png')
    def start(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1 and (0<pos[0]<50) and (0<pos[1]<50):
                self.screen.blit(self.image, (0,0))
                pygame.display.update()

                print(pos)
