from turtle import Screen
import time, food, snake, score_board

snake = snake.Snake()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('orange')
screen.title('Snake Game!!')
screen.listen()
screen.tracer(0)
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


food = food.Food()

score = score_board.Score()

game_is_on = True
count = 0
while game_is_on:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.eaten()
        snake.grow()
        score.update_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False
    # Detect collision with body
    for _ in snake.segments[1:]:
        if snake.head.distance(_) < 10:
            score.game_over()
            game_is_on = False
    time.sleep(0.13)


screen.exitonclick()