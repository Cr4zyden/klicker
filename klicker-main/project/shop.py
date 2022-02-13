import pygame

class Shop:
    def __init__(self):
        self.image = pygame.image.load('img/shop.png')
        self.back_button = pygame.image.load('img/back.png')
        self.back_button_pos = (0,0)
        self.damage = pygame.image.load('img/damage.png')
        self.damage_pos = (50,50)
        self.touch = pygame.image.load('img/touch.png')
        self.touch_pos = (50,300)

    def text(self,screen,text,pos):
        font = pygame.font.SysFont('couriernew', 30)
        text_to_send = font.render(str(text), True, (255, 255, 255))
        screen.blit(text_to_send,pos)
    def draw(self,screen,balance,damage_percent,dps):
        screen.blit(self.back_button,self.back_button_pos)
        screen.blit(self.damage,self.damage_pos)
        screen.blit(self.touch,self.touch_pos)

        font = pygame.font.SysFont('couriernew', 30)
        text = font.render(str(f'balance:{balance}'), True, (255, 255, 255))
        screen.blit(text, (55, 0))
        self.text(screen,f'balance:{balance}',(55, 0))
        text = font.render(str(f'price:{100*damage_percent}'), True, (255, 255, 255))
        screen.blit(text, (50, 255))

        text = font.render(str('Множитель урона x2'), True, (255, 255, 255))
        screen.blit(text, (255, 50))

        text = font.render(str(f'Ваш множитель:{damage_percent}'), True, (255, 255, 255))
        screen.blit(text, (255, 80))

        text = font.render(str(f'price:{100*dps}'), True, (255, 255, 255))
        screen.blit(text, (50,505))

        text = font.render(str(f'Автоматический урон +1/сек'), True, (255, 255, 255))
        screen.blit(text, (260,305))

        text = font.render(str(f'Ваш авто.урон: {dps}'), True, (255, 255, 255))
        screen.blit(text, (260,335))

    def try_to_buy(self,type,balance,damage_percent,dps):
        if type == 'click':
            if balance - 100*damage_percent >= 0:
                return True
        elif type == 'auto':
            if balance - 100*dps >= 0:
                return True
        return False