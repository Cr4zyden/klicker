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

        self.interface = Interface()
        self.balance = self.interface.seed.count
        self.shop = Shop(self.screen,self.balance)
        self.boss = Boss(1)

        self.player_damage = 5
        self.player_per_sec = 0

    def try_to_click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(self.boss.health)
            self.draw_healt_bar()

            pos = pygame.mouse.get_pos()
            if event.button == 1  and (0 < pos[0] < 50) and (0 < pos[1] < 50):
                # self.screen.blit(self.image, (0,0))
                self.screen.fill((0, 0, 0))
                pygame.display.update()
            elif event.button == 1 or 2and (100 < pos[0] < 580) and (70 < pos[1] < 570):
                self.boss.bite(self.player_damage,self.screen)
                self.balance += self.boss.bite(self.player_damage,self.screen)
                self.draw_healt_bar()

    def draw_healt_bar(self):
        healt_percent = (self.boss.health/(50*self.boss.level))

        black_rect = pygame.Rect(500,60,300*(1-healt_percent),50)
        rect = pygame.Rect(500,60,300*healt_percent,50)
        white_rect = pygame.Rect(500,60,300,50)
        pygame.draw.rect(self.screen, (0, 255, 0), rect, 0)
        pygame.draw.rect(self.screen, (0, 0, 0), black_rect, 0)
        pygame.draw.rect(self.screen,(255,255,255),white_rect,5)

        pygame.display.update()

    def start(self):
        self.draw_healt_bar()
        font = pygame.font.SysFont('couriernew', 40)
        text = font.render(str('1'), True, (255,255,255))
        self.screen.blit(text, (75, 50))
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                else:
                    self.try_to_click(event)
    def draw(self):
        self.interface.draw(self.screen)
        self.boss.draw(self.screen)
        pygame.display.update()

main = Main()
main.start()