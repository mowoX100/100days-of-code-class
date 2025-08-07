from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = random.randint(-280, 280)
        self.y_pos = random.randint(-280, 280)
        self.shape('circle')
        self.penup()
        self.resizemode("user")
        self.shapesize(0.5, 0.5)
        self.goto(self.x_pos, self.y_pos)

    def eaten(self):
        new_x_pos = random.randint(-280, 280)
        new_y_pos = random.randint(-280, 280)
        self.goto(new_x_pos, new_y_pos)
