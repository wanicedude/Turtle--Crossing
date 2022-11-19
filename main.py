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
car = CarManager()
   

screen.onkey(player.move, "Up")
# print(cart)

game_is_on = True
while game_is_on:
    
    #creating multiple cars
    

    
    time.sleep(0.1)
    screen.update()
    car.move_car()
    car.create()
    


screen.exitonclick()
