import turtle
import time
from food import *
from snake import *

win = turtle.Screen()
win.title("Snake game")
width = 500
height = 500
win.setup(width=width, height=height)
win.bgcolor("green")

food = Food()

while True:
    win.update()
    time.sleep(0.1)

win.mainloop()