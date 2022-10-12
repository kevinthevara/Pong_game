from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_points = 0
        self.r_points = 0

    def update(self, l_increase, r_increase):
        self.clear()
        self.l_points += l_increase
        self.r_points += r_increase
        self.goto(-100, 200)
        self.write(self.l_points, True, "center", ("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_points, True, "center", ("Arial", 60, "normal"))