from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
    def create_car(self):
        random_choice = random.randint(1,10)
        if random_choice == 6:
            new_car = Turtle()
            new_car.shape("square")
            # change width of square
            # self.shapesize(1, 2)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()

            new_car.color(random.choice(COLORS))
            # self.setheading(180)
            y_position = random.randint(-250,250)
            new_car.goto(x=280, y=y_position)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)






