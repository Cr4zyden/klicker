import pygame

class Boss:
    def __init__(self,level):
        self.level = level
        self.health = 50 * level
        self.image = pygame.image.load('img/watermelon.png')
        self.pos = (200,100)

    def update_level(self,screen,):
        rect = pygame.Rect(50, 50, 50, 50)
        pygame.draw.rect(screen, (0, 0, 0), rect, 0)
        font = pygame.font.SysFont('couriernew', 40)
        text = font.render(str(self.level), True, (255, 255, 255))
        screen.blit(text, (50, 50))
    def draw(self,screen):
        screen.blit(self.image, self.pos)

    def bite(self,damage):
        self.health -= damage

        if self.health <= 0:
            self.level += 1
            self.health = 50 * self.level
            return 13 * (self.level-1)
        return 0