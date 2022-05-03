from turtle import Turtle
import random
colors = ['red','green','yellow','blue','orange','white','magenta']
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1.0,stretch_wid=1.0)
        self.color1=random.choice(colors)
        self.color(self.color1)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.color1 = random.choice(colors)
        self.color(self.color1)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)