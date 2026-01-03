import turtle
import time

win = turtle.Screen()
win.title("Snake game")
width = 500
height = 500
win.setup(width=width, height=height)
win.bgcolor("green")

while True:
    win.update()
    time.sleep(0.1)

win.mainloop()