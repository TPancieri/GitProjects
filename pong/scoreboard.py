from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 48, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 220)
        self.score_left = 0
        self.score_right = 0
        self.write(arg=f"{self.score_left} : {self.score_right}", move=False, align=ALIGNMENT, font=FONT)

    def score_refresh(self):
        self.clear()
        self.write(arg=f"{self.score_left} : {self.score_right}", move=False, align=ALIGNMENT, font=FONT)

    def left_scored(self):
        self.score_left += 1
        self.score_refresh()

    def right_scored(self):
        self.score_right += 1
        self.score_refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
