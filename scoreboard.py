from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        with open(file="data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open(file="data.txt", mode="w") as data:
            data.write(str(self.high_score))
        self.update_scoreboard()

