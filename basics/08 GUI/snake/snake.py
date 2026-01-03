import turtle

class Snake:
    def __init__(self, startX, startY):
        self.startX = startX
        self.startY = startY
        self.segments = []
        self.refresh()

    def refresh(self):
        print("Snake reset")

        self.segments = []
        self.addSegment(self.startX, self.startY)

    def addSegment(self, x, y):
        t = turtle.Turtle("square")
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.color("red")
        t.showturtle()
        self.segments.append(t)