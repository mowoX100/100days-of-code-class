from turtle import Screen, Turtle
import random

# colors extracted using colorgram.py
colors = [(193, 172, 123), (152, 96, 60), (182, 158, 54), (10, 52, 75), (56, 33, 26), (125, 37, 25), (124, 163, 175), (109, 69, 84), (33, 116, 159), (83, 134, 78), (73, 32, 39), (114, 37, 43), (76, 152, 122), (10, 60, 41), (182, 99, 84), (210, 202, 149)]

# setup
screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.penup()
tim.ht()
tim.speed('fastest')

y_pos = -145
x_pos = -195
gap = 40
tim.goto(x_pos, y_pos)
def pick_color():
    color = colors[random.randint(0, len(colors) - 1)]
    return color


for i in range(10):
    for j in range(10):
        tim.dot(20, pick_color())
        tim.fd(gap)
    y_pos += gap
    tim.goto(x_pos, y_pos)


screen.exitonclick()