from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 24, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.level = 0
        self.write(f"Level {self.level + 1}", align=ALIGNMENT, font=FONT)

    def game_over_screen(self):
        self.clear()
        self.home()
        self.write(f"   GAME OVER    \n FINAL LEVEL : {self.level + 1}", align=ALIGNMENT, font=FONT)

    def winner_screen(self):
        self.clear()
        self.home()
        self.write(f" YOU WIN !!! ", align=ALIGNMENT, font=FONT)

    def level_count_reset(self):
        self.clear()
        self.write(f"Level {self.level + 1}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.level_count_reset()
