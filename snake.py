from turtle import Turtle
MOVE = 20
STRATING_POS = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
         for pos in STRATING_POS:
             self.add_segment(pos)
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("palegreen")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # This part moves the tail segments forward to the position of the one in front
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # Removed the 'segment ='

        # This part actually moves the head forward
        self.head.forward(MOVE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Send old segments off-screen
        self.segments.clear()  # Clear the list
        self.create_snake()  # Re-initialize starting segments
        self.head = self.segments[0]
