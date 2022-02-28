from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # give position to turtle
        # not draw line
        self.penup()
        self.goto(0,-280)
        # turtle change direction north
        self.left(90)

    def moveUp(self):
        self.forward(20)