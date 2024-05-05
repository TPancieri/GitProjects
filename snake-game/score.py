from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 350)
        self.score = 0
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
