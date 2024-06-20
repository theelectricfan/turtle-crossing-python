import turtle
from foothpath import Footpath
from player import Player
from carManager import CarManager
from information import Information

screen = turtle.Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
footpath = Footpath()

information = Information()

player = Player()

level = 1

key_states = {
    "move_up": False,
    "move_down": False
}


def update_key_state(key, state):
    key_states[key] = state


def move_turtle():
    if key_states["move_up"]:
        player.go_up()
    if key_states["move_down"]:
        player.go_down()


def detectCollision(car):
    if player.distance(car) <= 20:
        return True
    else:
        return False


def collisionDetector(carManager):
    for car in carManager.current_cars:
        if detectCollision(car):
            return True
    return False


screen.listen()

def game():
    global level
    information.writeLevel(level)

    carManager = CarManager()

    screen.onkeypress(lambda: update_key_state("move_up", True), "Up")
    screen.onkeypress(lambda: update_key_state("move_down", True), "Down")
    screen.onkeyrelease(lambda: update_key_state("move_up", False), "Up")
    screen.onkeyrelease(lambda: update_key_state("move_down", False), "Down")

    game_on = True

    carManager.spawn_car(screen)

    while game_on:
        screen.update()
        move_turtle()
        carManager.move_cars(level)
        carManager.remove_cars()
        if collisionDetector(carManager):
            information.writeGameOver(level)
            game_on = False

        if player.ycor() > 300:
            level += 1
            information.writeLevel(level)
            player.goto(0, -280)


game()

screen.update()
screen.exitonclick()
