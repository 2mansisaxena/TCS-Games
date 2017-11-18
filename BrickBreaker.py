from tkinter import *
import random



class Bricks:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,7,40,27, fill = color, width = 2)
        
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(200,405,300,415, fill = "blue")
        self.x = 0
        self.p = 0
        self.canvas.bind_all("<Left>", self.left)
        self.canvas.bind_all("<Right>", self.right)
        self.canvas.bind_all("<space>", self.pause)
    def left(self, event):
        self.x = -10
    def right(self, event):
        self.x = 10
    def draw(self):
        position = self.canvas.coords(self.id)
        if (position[2]+self.x>500) or (position[0]+self.x<0):
            self.x = 0
        self.canvas.move(self.id,self.x,0)
        self.x = 0
        
    def pause(self, event):
        self.p += 1
        if self.p == 2:
            self.p = 0

class Ball:
    def __init__(self,canvas, brickList, paddle, score):
        self.canvas = canvas
        self.bricks = brickList
        self.paddle = paddle
        self.score = score
        self.scorevalue = 0
        self.flag = True
        self.x = .5
        self.y = -.5
        self.id = canvas.create_oval (243, 391, 257, 405, fill = "white")
    def draw(self):
        position = self.canvas.coords(self.id)
        self.canvas.move(self.id,self.x,self.y)
        if (position[2]>500):
            self.x = -.5
        if (position[0]<0):
            self.x = .5
        if (position[1]<0):
            self.y = .5
        if (position[3]>415):
            self.flag = False
        if self.hitPaddle(position):
            self.y = -.5
        if self.hitBrick(position):
            self.y = -self.y
    def hitPaddle(self, position):
        paddlepos = self.canvas.coords(self.paddle.id)
        if (position[3] == paddlepos[1]) and (position[2]>=paddlepos[0]) and (position[0]<=paddlepos[2]):
            return True
        else:
            return False
    def hitBrick(self, position):
        for line in self.bricks:
            for brick in line:
                brickpos = self.canvas.coords(brick.id)
                try:
                    if (position[0] <= brickpos[2]) and (position[2]>=brickpos[0]):
                        if (position[1] < brickpos[3]) and (position[3]> brickpos[1]):
                            self.scorevalue += 1
                            self.score.configure(text = "Score: " + str(self.scorevalue))
                            self.canvas.delete(brick.id)
                            return True
                except:
                    continue
        return False
        



def game(event):
    canvas.delete("all")
    score.configure(text = "Score: 0")
    paddle = Paddle(canvas)
    brickList = []
    brickColors = ["red", "OrangeRed2", "salmon",
                   "indian red", "coral", "goldenrod1",
                   "firebrick2", "indianred2", "brown3",
                   "pale violet red", "darkGoldenrod1",
                   "sienna2", "brown4", "yellow"]
    for r in range(4):
        rowList = []
        for i in range(14):
            brick = Bricks(canvas, brickColors[i])
            rowList.append(brick)
        brickList.append(rowList)
        random.shuffle(brickColors)
    for r in range(4):
        for i in range(14):
            canvas.move(brickList[r][i].id, 35*i, 25*r)
    ball = Ball(canvas, brickList, paddle, score)
    while True:
        if paddle.p != 1:
            try:
                canvas.delete(message)
                del message
            except:
                pass
            paddle.draw()
            ball.draw()
            if not (ball.flag):
                end = canvas.create_text(250,250, text = "GAME OVER", fill = "white", font = "Arial 24 bold")
                break
            root.update_idletasks()
            root.update()
        else:
            try:
                if message==None:pass
            except:
                message = canvas.create_text(250,250, text = "PAUSE", fill = "green", font = "Arial 24 bold")
            root.update_idletasks()
            root.update()


root = Tk()
root.title("BrickBreaker")
root.geometry("530x500")
root.resizable(0,0)
canvas = Canvas(root, width = 500, height = 415, bg = "black")
canvas.pack()
score = Label(width = 40, height = 75, text = "Score: 0", font = "Georgia 14 bold")
score.pack(side = "left")

root.bind_all("<Return>",game)

root.mainloop()



