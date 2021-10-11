from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()

    # TODO 3: Create Food

    def refresh(self):
        self.penup()
        self.setpos(randint(-280, 280), randint(-280, 280))
        self.shape('circle')
        self.shapesize(0.75)
        self.color('blue')
