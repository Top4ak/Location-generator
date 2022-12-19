import math
from classes import * 

def DrawBezier(p0, p1, p2, p3):
    x = p0.x
    y = p0.y
    t = 0
    ts = 0.04

    while t <= 1.0:
        
        B0 = 1 * math.pow((1 - t), 3) 
        B1 = 3 * math.pow((1 - t), 2) * math.pow(t, 1)
        B2 = 3 * math.pow((1 - t), 1)  * math.pow(t, 2)
        B3 = 1 * math.pow(t, 3)
       
        x = int(p0.x*B0 + p1.x*B1 + p2.x*B2 + p3.x*B3)
        y = int(p0.y*B0 + p1.y*B1 + p2.y*B2 + p3.y*B3)
        
        goto(x, y)
        t=t+ts