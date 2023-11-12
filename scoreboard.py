from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.sety(250)
        self.pencolor("white")
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    # def end_game(self):
    #     game_over = Turtle()
    #     game_over.color("white")
    #     game_over.write("GAME OVER", move=False, align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
        with open("highscore.txt", mode="w") as data:
            data.write(f"{self.high_score}")
