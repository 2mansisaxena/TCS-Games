import pygame
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
orange = (255, 128, 0)
violet = (110, 8, 137)
class Wall (pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Room ():
    wallList = None
    def __init__ (self):
        self.wallList = pygame.sprite.Group()

class Room2(Room):
    def __init__ (self):
        super().__init__()
        walls = [[500, 25, violet, 0, 0], #top
                 [500, 25, violet, 0, 475], #bottom
                 [25, 235, violet, 0, 250], #left bottom
                 [25, 205, violet, 0, 0], #left top
                 [25, 205, violet, 475, 0], #right top
                 [25, 235, violet, 475, 250]] #right bottom
        for i in walls:
            wall = Wall(i[0],i[1],i[2],i[3],i[4])
            self.wallList.add(wall)
        for x in range(95, 450, 95):
            for y in range (65, 280, 205):
                 wall = Wall(25, 165, white, x, y)
                 self.wallList.add(wall)
        for x in range(145, 420, 95):
            wall = Wall(20, 160, orange, x, 170)
            self.wallList.add(wall)

class Room1 (Room):
    def __init__ (self):
        super().__init__()
        walls = [[500, 25, violet, 0, 0], #top
                 [500, 25, violet, 0, 475], #bottom
                 [25, 235, violet, 0, 250], #left bottom
                 [25, 205, violet, 0, 0], #left top
                 [25, 205, violet, 475, 0], #right top
                 [25, 235, violet, 475, 250],
                 [20, 300, white, 155, 25],
                 [20, 300, white, 315, 175]]
        for i in walls:
            wall = Wall(i[0],i[1],i[2],i[3],i[4])
            self.wallList.add(wall)

class Room3 (Room):
    def __init__ (self):
        super().__init__()
        walls = [[500, 25, violet, 0, 0], #top
                 [500, 25, violet, 0, 475], #bottom
                 [25, 235, violet, 0, 250], #left bottom
                 [25, 205, violet, 0, 0], #left top
                 [25, 205, violet, 475, 0], #right top
                 [25, 235, violet, 475, 250]] #right bottom
        self.rows = 10
        self.cols = 10
        for i in walls:
            wall = Wall(i[0],i[1],i[2],i[3],i[4])
            self.wallList.add(wall)
        self.maze()
    def maze(self):
        file = open("Maze3.txt")
        lines = []
        for line in file:
            lines.append(line)
        for i in range(len(lines)):
            for j in range(len(line)):
                if lines[i][j] == "s":
                    wall = Wall (45, 45, orange, (j*45)+25, (i*45)+25)
                    self.wallList.add(wall)

class Changeroom (Room):
    def __init__ (self):
        super().__init__()
        walls = [[500, 25, violet, 0, 0], #top
                 [500, 25, violet, 0, 475], #bottom
                 [25, 235, violet, 0, 250], #left bottom
                 [25, 205, violet, 0, 0], #left top
                 [25, 205, violet, 475, 0], #right top
                 [25, 235, violet, 475, 250]]
        self.addText()
        textsurface1 = None
        textsurface2 = None
        for i in walls:
            wall = Wall(i[0],i[1],i[2],i[3],i[4])
            self.wallList.add(wall)
    def addText(self):
        myfont1 = pygame.font.SysFont("Times New Roman", 20)
        self.textsurface1 = myfont1.render("<= Last Room", True, red)
        myfont2 = pygame.font.SysFont("Times New Roman", 20)
        self.textsurface2 = myfont2.render("First Room =>", True, red)        


class Player (pygame.sprite.Sprite):
    changex = 0
    changey = 0
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.image.load("turtle.png").convert()
        self.image = pygame.transform.scale(self.image, (20,12))
#        self.image = pygame.Surface([15,15])
#        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = -1
    def movePlayer(self, walls):
        if self.changex > 0:
            if self.direction == -1:
                self.flipPlayer()
                self.direction = 1
        if self.changex < 0:
            if self.direction == 1:
                self.flipPlayer()
                self.direction = -1
        self.rect.x += self.changex
        collisionList = pygame.sprite.spritecollide(self, walls, False)
        for wall in collisionList:
            sound.play()
            if self.changex >= 0:
                self.rect.right = wall.rect.left
            if self.changex < 0:
                self.rect.left = wall.rect.right
        self.rect.y += self.changey
        collisionList = pygame.sprite.spritecollide(self, walls, False)
        for wall in collisionList:
            sound.play()
            if self.changey < 0:
                self.rect.top = wall.rect.bottom
            if self.changey >= 0:
                self.rect.bottom = wall.rect.top
    def alterSpeed (self, x, y):
        self.changex += x
        self.changey += y
    def flipPlayer (self):
        self.image = pygame.transform.flip(self.image, True, False)


pygame.mixer.init()
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500,500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption('Maze Runner')

rooms = []
room1 = Room1()
rooms.append(room1)
room2 = Room2()
rooms.append(room2)
room3 = Room3()
rooms.append(room3)
changeroom = Changeroom()
rooms.append(changeroom)

player1 = Player(20,215)

sprite = pygame.sprite.Group()
sprite.add(player1)

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

roomnumber = 0
currentRoom = rooms[roomnumber]
sound = pygame.mixer.Sound("boing_x.wav")
while not done:
    # --- Main event loop
    for event in pygame.event.get():
#        print (event)
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.alterSpeed(0,-2)
            if event.key == pygame.K_DOWN:
                player1.alterSpeed(0,2)
            if event.key == pygame.K_LEFT:
                player1.alterSpeed(-2,0)
##                if player1.direction == 1:
##                    player1.flipPlayer()
##                    player1.direction = -1
            if event.key == pygame.K_RIGHT:
                player1.alterSpeed(2,0)
##                if player1.direction == -1:
##                    player1.flipPlayer()
##                    player1.direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1.alterSpeed(0,2)
            if event.key == pygame.K_DOWN:
                player1.alterSpeed(0,-2)
            if event.key == pygame.K_LEFT:
                player1.alterSpeed(2,0)
            if event.key == pygame.K_RIGHT:
                player1.alterSpeed(-2,0)

    if player1.rect.x >501 and roomnumber != len(rooms)-1:
        roomnumber += 1
        currentRoom = rooms[roomnumber]
        player1.rect.x = 5

    if player1.rect.x >501 and roomnumber == len(rooms)-1:
        roomnumber = 0
        currentRoom = rooms[roomnumber]
        player1.rect.x = 5
        
    if player1.rect.x < -2 and roomnumber == 0:
        roomnumber = len(rooms)-1
        currentRoom = rooms[roomnumber]
        player1.rect.x = 495
        
    if player1.rect.x < -2 and roomnumber > 0:
        roomnumber -= 1
        currentRoom = rooms[roomnumber]
        player1.rect.x = 495


    player1.movePlayer(currentRoom.wallList)
    screen.fill(black)
    if roomnumber == len(rooms)-1:
        screen.blit(currentRoom.textsurface1, (15,220))
        screen.blit(currentRoom.textsurface2, (373,220))
    currentRoom.wallList.draw(screen)
    sprite.draw(screen)

    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
