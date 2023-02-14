COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random



class CarManager():
    def __init__(self) -> None:
        
        
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def generate_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            random_color = random.choice(COLORS)
            random_y = random.randint(-250, 250)
            new_car = Turtle("square")
            #new_car.resizemode("user")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random_color)
            new_car.setheading(180)
            new_car.goto(280, random_y)
            self.car_list.append(new_car)
            
    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)
            
    def move_increment(self):
        self.car_speed += MOVE_INCREMENT
