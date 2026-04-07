from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 16, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.update_score()
    def score_up(self):
        self.clear()
        self.score += 1
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.write("Game Over!!", align=ALIGNMENT, font=FONT)