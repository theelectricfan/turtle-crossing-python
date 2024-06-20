import turtle
import random
from cars import Car


class CarManager():
    def __init__(self):
        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown",
                       "gray", "cyan", "magenta", "gold", "violet", "indigo", "lime", "maroon",
                       "navy", "olive", "teal", "silver", "coral", "salmon", "khaki", "orchid", "plum"]

        self.car_spawn = [[320, -245], [320, -215], [-320, -145], [-320, -115], [320, -45], [320, -15], [-320, 55],
                          [-320, 85], [320, 155], [320, 185], [-320, 255], [-320, 285]]

        self.car_angle = [180, 180, 0, 0, 180, 180, 0, 0, 180, 180, 0, 0]

        self.current_cars = []

    def spawn_car(self, screen):

        randomCar = random.randint(0, 11)

        # if self.occupied_lane[randomCar] == 0:
        random_color = random.choice(self.colors)
        random_spawn = self.car_spawn[randomCar]
        angle = self.car_angle[randomCar]
        car = Car(random_spawn[0], random_spawn[1], angle, random_color)
        self.current_cars.append(car)

        screen.ontimer(lambda: self.spawn_car(screen), 300)

    def move_cars(self, level):
        for car in self.current_cars:
            car.move_car(level)

    def remove_cars(self):
        for car in self.current_cars:
            if car.xcor() < -320 or car.xcor() > 320:
                self.current_cars.remove(car)
                car.hideturtle()
                del car
