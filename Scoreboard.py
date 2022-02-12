from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        pos_x = 0
        pos_y = 270
        self.penup()
        self.goto(pos_x, pos_y)
        self.hideturtle()
        self.update_scoreboard()


    def game_is_over(self):
        self.goto(0,0)
        self.write("Game over!", move=False, align="center", font=("Courier", 15, "normal"))

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 12, "normal"))