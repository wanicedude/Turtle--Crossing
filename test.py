
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


random_no = random.randint(0, len(COLORS)-1)
random_xcor = random.randint(-300, 300)
random_ycor = random.randint(-250, 250)
cor = (random_xcor, random_ycor)
print(cor)