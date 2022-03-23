from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 21, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.count = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.setposition(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.count} , High Score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def current_score(self):
        self.clear()
        self.count = self.count + 1
        self.update_score()

    def reset_score(self):
        if self.high_score < self.count:
            self.high_score = self.count
            with open("data.txt", mode="w") as data2:
                data2.write(f"{self.high_score}")
        self.clear()
        self.count = 0
        self.update_score()
