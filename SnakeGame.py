import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

segment_width = 15
segment_height = 15
segment_margin = 1

x_change = 0
y_change = 0

class Segment (pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

done = False
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

snake_segments = []

for i in range(10):
    segment = Segment (125 + segment_width*i, 0)
    snake_segments.append(segment)
    all_sprites_list.add(segment)

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width) *1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height) * 1

    old_segment = snake_segments.pop()
    all_sprites_list.remove(old_segment)

    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    if x <0:
        x = 400
    if y<0:
        y = 400
    if x >400:
        x = 0
    if y >400:
        y = 0
    segment = Segment (x,y)

    snake_segments.insert(0,segment)
    all_sprites_list.add(segment)
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
