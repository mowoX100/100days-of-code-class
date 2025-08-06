from turtle import Turtle, Screen
import random


screen = Screen()
colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
timmies = []
x_pos = -300
y_pos = -100
for i in range(6):
    tim = Turtle()
    timmies.append(tim)
    tim.color(colours[i])
    tim.shape('turtle')
    tim.penup()
    tim.goto(x_pos, y_pos)
    y_pos += 60


game_on = True
while game_on:
    for i in timmies:
        if i.xcor() < 200:
            i.fd(random.randint(0, 10))
        else:
            print(f'Race won by {i.color()} timmy')
            game_on = False

screen.exitonclick()
