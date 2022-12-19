from turtle import *

class Tree:
    def __init__(self, wind, branches):
        self.wind = wind
        self.branches = branches

    def paintTree(self):
        forward(10)

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