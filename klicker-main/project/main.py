import pygame

from interface import Interface
from shop import Shop
from boss import Boss

class Main():
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.active_window = "game"
        self.damage_percent = 1

        self.interface = Interface()
        self.balance = 0
        self.shop = Shop()
        self.boss = Boss(1)

        self.player_damage = 5
        self.player_per_sec = 1

    def try_to_click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.draw_healt_bar()

            pos = pygame.mouse.get_pos()
            if self.active_window == 'shop':
                if event.button == 1 and (0 < pos[0] < 50) and (0 < pos[1] < 50):
                    self.active_window = 'game'
                elif event.button == 1 and (50 < pos[0] < 250) and (50 < pos[1] < 250):
                    if self.shop.try_to_buy('click',self.balance,self.damage_percent,self.player_per_sec):
                        self.balance -= 100*self.damage_percent
                        self.damage_percent += 1
                elif event.button == 1 and (50 < pos[0] < 250) and (255 < pos[1] < 505):
                    if self.shop.try_to_buy('auto',self.balance,self.damage_percent,self.player_per_sec):
                        self.balance -= 100*self.player_per_sec
                        self.player_per_sec += 1

            else:
                if event.button == 1 and (0 < pos[0] < 50) and (0 < pos[1] < 50):
                    self.active_window = 'shop'

                elif event.button == 1 and (200 < pos[0] < 580) and (70 < pos[1] < 570):
                    self.balance += self.boss.bite(self.player_damage*self.damage_percent)
                    #self.balance += self.boss.bite(self.player_damage)

    def draw_healt_bar(self):
        healt_percent = (self.boss.health/(50*self.boss.level))
        black_rect = pygame.Rect(500,60,300*(1-healt_percent),50)
        rect = pygame.Rect(500,60,300,50)
        white_rect = pygame.Rect(500,60,300,50)
        pygame.draw.rect(self.screen, (0, 255, 0), rect, 0)
        pygame.draw.rect(self.screen, (0, 0, 0), black_rect, 0)
        pygame.draw.rect(self.screen,(255,255,255),white_rect,5)

    def draw(self):
        if self.active_window == 'game':
            self.screen.fill((0,0,0))
            self.interface.draw(self.screen)
            self.boss.draw(self.screen)
            self.draw_healt_bar()
            self.boss.update_level(self.screen)
        else:
            self.screen.fill((0,0,0))
            self.shop.draw(self.screen,self.balance,self.damage_percent,self.player_per_sec)

        pygame.display.update()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                else:
                    self.try_to_click(event)

            self.draw()
main = Main()
main.start()