import pygame
import random
import math

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
        self.rect = pygame.draw.circle(self.image,(random.randint(1, 255), random.randint(1, 255), random.randint(1, 250)), (8,8),7)
        self.rect.x = x
        self.rect.y = y
        
class Bullet (pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.Surface ((5,10))
        self.rect = pygame.draw.ellipse(self.image, (0,0,10), (3,5,5,10))
        self.rect.x = x
        self.rect.y = y

class Cannon (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.angle = 0
        self.image = pygame.Surface ((20,40))
        self.rect = self.image.get_rect()
        self.image.fill (blue)
        self.image0 = self.image.convert_alpha()
    def update(self):
        mousepos = pygame.mouse.get_pos()
        if mousepos[1] < 450: 
            self.angle = getAngle(mousepos[0], mousepos[1], self.rect.x, self.rect.y)
            self.image = pygame.transform.rotate(self.image0, self.angle)
            self.rect = self.image.get_rect()
            self.rect.center = (250,460)


def getAngle(x2,y2,x1,y1):
    rise = y2-y1
    run = x2-x1
    angle = math.atan2(run,rise)*(180/math.pi)
    angle = (angle)%180
#    print (angle)
    return angle

pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size)
done = False

spriteList = pygame.sprite.Group()
targetList = pygame.sprite.Group()
for i in range(40):
    target = Target(random.randint(10,490),random.randint(10,300))
    targetList.add (target)
    spriteList.add (target)

cannon1 = Cannon()
cannon1.rect.x = 235
cannon1.rect.y = 460

spriteList.add (cannon1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#        if event.type == pygame.MOUSEBUTTONDOWN
#    print (targetList)
    spriteList.update()
    screen.fill(black)
    spriteList.draw(screen)
    targetList.draw(screen)

##    screen.blit(tester.image, (250,250))
##    screen.blit(shooter.image, (235, 475))
##    screen.blit(cannon1.image, cannon1.rect.center)
    pygame.display.flip()
    

pygame.quit()
