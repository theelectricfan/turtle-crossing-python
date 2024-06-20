import turtle


class Footpath(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.pensize(40)
        for i in range(7):
            self.penup()
            self.goto(-300, -280 + i * 100)
            self.pendown()
            self.forward(600)

