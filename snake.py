from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]




    def create_snake(self):
      for position in STARTING_POSITIONS:
        self.add_segment(position)


    def add_segment(self,position):
        new_t = Turtle("square")
        new_t.penup()
        new_t.color('white')
        new_t.goto(position)
        self.segments.append(new_t)

    def extend(self):
        # add a new segment
        self.add_segment(self.segments[-1].position())


    def move(self):
        for t_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[t_num - 1].xcor()
            new_y = self.segments[t_num - 1].ycor()
            self.segments[t_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)