import turtle


class Car(turtle.Turtle):
    def __init__(self, x, y, angle, color):
        super().__init__()
        self.shape("square")
        self.setheading(angle)
        self.shapesize(1, 2)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.showturtle()

    def move_car(self, level):
        self.forward(0.05 * level)