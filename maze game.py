from pygame import *
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

class Wall (sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.surface = Surface([width, height])
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

class Room ():
    wallList=None
    def __init__ (self):
        self.wallList = sprite.Group()

class Room1(Room):
    def __init__ (self):
        super().__init__()
        walls = [[500, 10, white, 0, 0],
                 [500, 10, white, 0, 490],
                 [10, 240, white, 0, 260],
                 [10, 240, white, 0, 0],
                 [10, 240, white, 490, 0],
                 [10, 240, white, 490, 260]]
        for i in walls:
            print (i[0],i[1])
            wall = Wall(i[0],i[1],i[2],i[3],i[4])
            self.wallList.add(wall)
init()
# Create an 800x600 sized screen
screen = display.set_mode([800, 600])

# Set the title of the window
display.set_caption('Maze Runner')

room1 = Room1()

clock = time.Clock()
done = False
while not done:
    # --- Event Processing ---
    for event in event.get():
        if event.type == QUIT:
            done = True
    # --- Drawing ---
    screen.fill(black)
 
#    movingsprites.draw(screen)
#    room1.wallList.draw(screen)
 
    display.flip()
 
    clock.tick(60)
 
quit()
