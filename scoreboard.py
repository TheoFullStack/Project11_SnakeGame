from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f'Score: {self.score}', align= ALIGNMENT, font= FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updatescoreboard()