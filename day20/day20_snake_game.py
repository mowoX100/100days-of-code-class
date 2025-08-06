from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('orange')
screen.title('Snake Game!!')
screen.tracer(0)


segments = []
positions = [(0, 0), (-20, 0), (-40, 0)]
for segment_position in positions:
    segment = Turtle('square')
    segment.color('blue')
    segment.penup()
    segment.goto(segment_position)
    segments.append(segment)
# screen.update()

game_is_on = True
count = 0
while count < 15:
    screen.update()

    for i in range(len(segments) - 1, 0, -1):
        prev = i - 1
        per_xcord = segments[prev].xcor()
        per_ycord = segments[prev].ycor()
        segments[i].goto(per_xcord , per_ycord)
    segments[0].fd(20)
    count += 1
    time.sleep(0.5)


screen.exitonclick()