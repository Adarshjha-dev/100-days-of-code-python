from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)

    def up(self):
        y = self.ycor()
        if y < 240:
            self.sety(y + 20)

    def down(self):
        y = self.ycor()
        if y > -240:
            self.sety(y - 20)
