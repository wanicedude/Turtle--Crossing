from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
       
        

    def create(self):
        """Create car
        """
        
        
        random_chance = random.randint(1,6)
        if random_chance == 1:  #Create car at every time the while loop as been run 6 times
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_no = random.randint(0, len(COLORS)-1)
            random_ycor = random.randint(-250, 250)
            new_car.color(COLORS[random_no])
            new_car.goto(300, random_ycor)
            new_car.setheading(180)
            self.all_cars.append(new_car)
        
        
            

    def move_car(self):
        for car in self.all_cars:
            global STARTING_MOVE_DISTANCE
            car.forward(self.car_speed)
            
            
    def increase_speed (self):
       self.car_speed += MOVE_INCREMENT
           
