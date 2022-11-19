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
    
    # Detect when turtle as reached the top of the screen and go back to starting position
    if player.ycor() == 300:
        player.goto((0, -280))
        car_manager.increase_speed()
        


screen.exitonclick()
