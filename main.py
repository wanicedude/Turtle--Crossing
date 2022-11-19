import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from itertools import count

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


# cart = []
player = Player()
car_manager = CarManager()
   

screen.onkey(player.move, "Up")
# print(cart)

game_is_on = True
while game_is_on:
    
    #creating multiple cars
    

    
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    car_manager.create()
    
    #Detect  collision cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


screen.exitonclick()
