from random import randint
from turtle import *
from math import *
from classes import *
from algo import *



speed(0)
screensize(1400, 800)
setup(1440, 840)     # +30 +30
print(window_height(), window_width())

bgcolor("black")

def proga():
   colormode(255)
   pencolor(255, 255, 255)

   while(True):
      reset()
      pensize(15)
      ht()
      a = []
      x = -700
      while(x < 550):
         tmp = randint(-300, 300)
         a.append(xy(x - 100, tmp))
         a.append(xy(x, tmp))
         a.append(xy(x + 100, tmp))
         x += randint(150, 300)
      
      tmp = randint(-300, 300)
      a.append(xy(600, tmp))
      a.append(xy(700, tmp))

      pu()
      goto(a[1].x, a[1].y)
      pd()

      for i in range(1, len(a) - 2, 3):
         DrawBezier(a[i], a[i + 1], a[i + 2], a[i + 3])


   #col = Gradient(0, 255, 0, 105, 105, 105)
   col = Gradient(0, 255, 0, 128, 128, 128)

   #while xcor() < 700:
      

   
   
proga()
exitonclick()