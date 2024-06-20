import turtle

class Information(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.hideturtle()

    def writeLevel(self, level):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {level}", align="center", font=("Arial", 24, "normal"))

    def writeGameOver(self, level):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER \nLevel: {level}", align="center", font=("Arial", 24, "normal"))