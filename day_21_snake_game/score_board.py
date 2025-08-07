from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 280
        self.penup()
        self.ht()
        self.score = -1
        self.goto(self.x_pos, self.y_pos)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'score = {self.score}', align='center', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 15, 'normal'))
