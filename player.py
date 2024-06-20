import turtle


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def go_up(self):
        self.forward(0.1)

    def go_down(self):
        self.backward(0.1)