from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.write(f"Game Over!! your total score is: {self.score}", align="center", font=("Arial", 24, "normal"))