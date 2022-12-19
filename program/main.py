from random import randint
from turtle import *
from math import *
import time
from turtle import _Screen
from classes import *



speed(0)
screensize(1400, 800)
setup(1440, 840)     # +30 +30
print(window_height(), window_width())

bgcolor("black")

def proga():
   colormode(255)
   pencolor(255, 255, 255)
   pensize(10)

   goto(-700, 0)

   a = []
   i = -700
   while(i < 550):
      a.append(xy(i, randint(-300, 300)))
      i += randint(100, 200)
   a.append(xy(700, randint(-300, 300)))
   



   #col = Gradient(0, 255, 0, 105, 105, 105)
   col = Gradient(0, 255, 0, 128, 128, 128)

   #while xcor() < 700:
      

   
   
proga()
exitonclick()