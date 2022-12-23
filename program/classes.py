from turtle import *
from random import randint

class Tree:
    def __init__(self, wind, branches):
        self.wind = wind
        self.branches = branches

    def paintTree(self):
        pencolor(round(92/1.5), round(64/1.5), round(51/1.5))
        a = []      #array of branches
        x = 7
        while x < 13:       #generating random count of branches im main trunk
            a.append(x)
            x += randint(2, 5)
        x = 0
        a.append(14)

        for i in range(15):
            forward(15)
            pensize(17 - round(i / 2))
            if(x < len(a) and i == a[x]):       #its time to make branch 
                tmp = randint(-20, 20)
                if(randint(0, 2) < 2):
                    right(40 + tmp)
                    self.__branch((300 - i * 15) * randint(4, 7) / 10, 0, len(a) - x, 17 - round(i / 2) - 1)
                    left(40 + tmp)

                if(randint(0, 2) < 2):
                    left(40 + tmp)
                    self.__branch((300 - i * 15) * randint(4, 7) / 10, 0, len(a) - x, 17 - round(i / 2) - 1)
                    right(40 + tmp)
                x += 1
                pensize(17 - round(i / 2))

        back(15*15)
        pensize(15)

    def __branch(self, size, step, maxStep, ps):
        if(step >= maxStep): 
            return
        pensize(ps)
        forward(size)
        tmp = randint(-10, 10)
        if(randint(0, 3) < 3):
            right(30 + tmp)
            self.__branch(size * randint(4, 7) / 10, step + 1, maxStep, ps - 3)
            left(30 + tmp)
        if(randint(0, 3) < 3):
            left(30 + tmp)
            self.__branch(size * randint(4, 7) / 10, step + 1, maxStep, ps - 3)
            right(30 + tmp)
        
        back(size)
        pensize(ps)
        


class xy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rgb:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Gradient:
    def __init__(self, r0, g0, b0, r1, g1, b1):
        self.firstColor = Rgb(r0, g0, b0)
        self.secondColor = Rgb(r1, g1, b1)
        self.curColor = Rgb(0, 0, 0)
    
    def updateColor(self, cur, mn = 0, mx = 1):     #cur (from 0 to 1) is percentage value of gradient 
        cur = (cur - mn) / (mx - mn)
        if(cur < 0): 
            cur = 0
        elif(cur > 1): 
            cur = 1
        
        #print(float(self.secondColor.r - self.firstColor.r) * cur, float(self.secondColor.g - self.firstColor.g) * cur, float(self.secondColor.b - self.firstColor.b) * cur)
        self.curColor.r = self.firstColor.r + round(float(self.secondColor.r - self.firstColor.r) * cur)
        self.curColor.g = self.firstColor.g + round(float(self.secondColor.g - self.firstColor.g) * cur)
        self.curColor.b = self.firstColor.b + round(float(self.secondColor.b - self.firstColor.b) * cur)