from turtle import Turtle


POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Constants in python are named using all caps
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('turtle')

    def create_snake(self):
        for segment_position in POSITIONS:
            self.add_segment(segment_position)

    def add_segment(self, position):
        segment = Turtle('circle')
        segment.color('blue')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        self.add_segment(self.segments[-1].pos())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            prev = i - 1
            previous_x_cord = self.segments[prev].xcor()
            previous_y_cord = self.segments[prev].ycor()
            self.segments[i].goto(previous_x_cord, previous_y_cord)
        self.head.fd(20)

