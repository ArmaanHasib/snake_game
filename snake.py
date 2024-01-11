from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_block = Turtle()
        snake_block.shape("square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.goto(position)
        self.snake_body.append(snake_block)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for block in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[block - 1].xcor()
            new_y = self.snake_body[block - 1].ycor()
            self.snake_body[block].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for self.block in self.snake_body:
            self.block.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

