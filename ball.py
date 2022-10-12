from turtle import Turtle, Screen

screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 5
        self.ymove = 5
        self.move_flash = 0.1

    def move_up(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_flash *= 0.8

    def start_position(self):
        self.goto(0, 0)
        self.move_flash = 0.1

