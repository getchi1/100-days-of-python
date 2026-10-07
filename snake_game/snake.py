from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.new_obj = []
        self.create_snake()
        self.head = self.new_obj[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.new_obj.append(timmy)

    def extend_snake(self):
        #add new segment to the snake
        self.add_segment(self.new_obj[-1].position())

    def move(self):
        """Starting from the last snake segment, move each segment to the previous segment's current position"""
        for obj_num in range(len(self.new_obj) - 1, 0, -1):
            new_x = self.new_obj[obj_num - 1].xcor()
            new_y = self.new_obj[obj_num - 1].ycor()
            self.new_obj[obj_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

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



