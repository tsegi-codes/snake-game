from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 16, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_tracker.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def score_up(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High_Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self ):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_tracker.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()