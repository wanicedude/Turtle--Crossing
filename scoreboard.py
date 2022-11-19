from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1 
        self.update_score()
        
    # def create_scoreboard(self):
    #     self.clear()
    #     self.goto(-230, 260)
    #     self.write(f"Level: {self.score}", align="center",
    #                font=(FONT))
        
        
    def update_score(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.score}", align="center",
                   font=(FONT))

    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def final_score(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Level: {self.score}", align="center",
                   font=(FONT))
        print(self.score)