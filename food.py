from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("lightpink")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-150, 150)
        random_y = random.randint(-150, 150)
        self.goto(random_x, random_y)