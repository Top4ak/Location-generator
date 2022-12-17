from turtle import *
from math import *
import time
from turtle import _Screen
speed(0)
screensize(1440, 810)
setup(1470, 840)     # +30 +30
print(window_height(), window_width())

bgcolor("orange")

def proga(x, step):
   right(45)      #angle
   forward(x)
   if(step < 8):
      proga(x * 0.7, step + 1)
   back(x)
   left(90)       #angle * 2
   forward(x)
   if(step < 8):
      proga(x * 0.7, step + 1)
   back(x)
   right(45)       #angle
   
   
left(90)
penup()
back(100)
pendown()
forward(120)
proga(100, 0)
goto(0,0)
exitonclick()