import pygame
import random

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
purple = (255,0,255)
orange = (255,128,0)
violet = (110,8,137)

class Target (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface ((15, 15))
        self.rect = pygame.draw.circle(self.image,(random.randint(1, 255), random.randint(1, 255), random.randint(1, 250)), (8,8), 7)
        
class Player (pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.Surface ((30,30))
        self.rect = pygame.draw.circle(self.image, blue, (15,15), 14)
        self.rect.x = x
        self.rect.y = y

#class Cannon (pygame.sprite.Sprite):
    
pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size)
done = False

tester = Target(250,250)
shooter = Player(235, 475)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(tester.image, (250,250))
    screen.blit(shooter.image, (235, 465))





    pygame.display.flip()
    

pygame.quit()
