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