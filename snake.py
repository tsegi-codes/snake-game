from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.starting_positions = [(0,0), (-20,0), (-40,0)]
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for position in self.starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)
    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            # self.move()
            self.head.setheading(UP)
            # self.move()
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            # self.move()
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # self.move()
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.move()
    def snake_grow(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        # last_x = self.segment[-1].xcor()
        # last_y = self.segment[-1].ycor()
        # new_segment.goto(last_x, last_y)
        self.segment.append(new_segment)

