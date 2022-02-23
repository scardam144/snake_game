from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 21, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.count = 0
        self.penup()
        self.setposition(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.count}", False, align=ALIGNMENT, font=FONT)

    def current_score(self):
        self.clear()
        self.count = self.count + 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
