from turtle import Turtle, Screen
screen = Screen()

keylist = ["Up", "Down", "w", "s"]


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(x, y)
        self.color("white")
        self.penup()

    def move(self, index):
        def up():
            newy = self.ycor() + 20
            self.goto(self.xcor(), newy)

        def down():
            newy = self.ycor() - 20
            self.goto(self.xcor(), newy)
        screen.listen()
        screen.onkeypress(up, keylist[index])
        screen.onkeypress(down, keylist[index+1])
