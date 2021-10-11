from turtle import Turtle


# TODO 5: Create a scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setpos(x=0, y=300)
        self.hideturtle()
        self.pencolor('white')
        self.write(arg=f"SCORE:{self.score}", align='center', font=('Century Gothic', 12, "bold"))

    def scorer(self):
        self.clear()
        self.score += 1
        self.write(arg=f"SCORE:{self.score}", align='center', font=('Century Gothic', 12, "bold"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.pencolor('cyan')
        self.write(arg=f"G A M E   O V E R", align='center', font=('Century Gothic', 36, "normal"))
