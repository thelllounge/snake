from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body_pieces = []
        self.create_snake()
        self.head = self.snake_body_pieces[0]

    def create_snake(self):
        for i in range(3):
            self.snake_body_pieces.append(Turtle("square"))
            self.snake_body_pieces[i].penup()
            self.snake_body_pieces[i].color("white")
            self.snake_body_pieces[i].setpos(STARTING_POSITIONS[i])

    def extend(self):
        self.snake_body_pieces.append(Turtle("square"))
        self.snake_body_pieces[-1].penup()
        self.snake_body_pieces[-1].color("white")
        self.snake_body_pieces[-1].setpos(self.snake_body_pieces[-2].pos())

    def move_forward(self):
        for position in range(len(self.snake_body_pieces) - 1, 0, -1):
            self.snake_body_pieces[position].goto(self.snake_body_pieces[position - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def face_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def face_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def face_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def face_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for piece in self.snake_body_pieces:
            piece.setpos((500, 500))
        self.snake_body_pieces.clear()
        self.create_snake()
        self.head = self.snake_body_pieces[0]