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
        file = open("data.txt", mode="r")
        self.high_score = file.read()
        file.close()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
        
    def increase_score(self):
        self.score += 1

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self) -> None:
        if self.score >int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh_score()

    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
