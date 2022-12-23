import math
from random import randint
from classes import * 

def DrawBezier(p0, p1, p2, p3):
    pd()
    x = p0.x
    y = p0.y
    t = 0
    ts = 0.02
    #--------------------------- 300
    #Gray
    #--------------------------- 240 
    #Green
    #--------------------------- -220
    #Blue
    #-------------------------- -300
    colGG = Gradient(0, 200, 0, 55, 55, 55)
    colGB = Gradient(30,144,255, 0, 200, 0)
    tree = Tree(2, 2)
    yLast = 0
    while t <= 1.0:
        
        B0 = 1 * math.pow((1 - t), 3) 
        B1 = 3 * math.pow((1 - t), 2) * math.pow(t, 1)
        B2 = 3 * math.pow((1 - t), 1)  * math.pow(t, 2)
        B3 = 1 * math.pow(t, 3)
       
        x = int(p0.x*B0 + p1.x*B1 + p2.x*B2 + p3.x*B3)
        y = int(p0.y*B0 + p1.y*B1 + p2.y*B2 + p3.y*B3)
        
        if(randint(0, 66) == 0 and abs(y - yLast) < 6):
            tmp = randint(-15, 15)
            left(90 + tmp)
            tree.paintTree()
            right(90 + tmp)

        colGG.updateColor(y, -270, 240)
        colGB.updateColor(y, -270, -220)
        if(y > -220):
            pencolor(colGG.curColor.r, colGG.curColor.g, colGG.curColor.b)
        else:
            pencolor(colGB.curColor.r, colGB.curColor.g, colGB.curColor.b)
        goto(x, y)
        t=t+ts

        yLast = y