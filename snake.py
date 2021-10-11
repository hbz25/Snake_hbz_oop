from turtle import Turtle, Screen
import time


class Snake:
    def __init__(self):
        # todo 01: Setup Screen and Ask difficulty level
        self.screen = Screen()
        self.screen.setup(width=600, height=650)
        self.screen.bgcolor('black')
        self.screen.title('Snake')
        self.screen.tracer(n=0)
        self.difficulty = self.screen.numinput(title='CHOOSE DIFFICULTY',
                                               prompt='enter 1 for easy, 2 for moderate and 3 for hard')
        self.speed = self.level(self.difficulty)
        # self.speed = 0.08
        # TODO 1: Create a Snake body
        self.body = []
        self.segments = 4
        self.make_snake(self.segments)
        self.head = self.body[0]

    def add_segments(self):
        snake_segment = Turtle(shape="square")
        # snake_segment.shapesize(.5)
        snake_segment.color('white')
        snake_segment.penup()
        self.body.append(snake_segment)

    def make_snake(self, segments):
        for n in range(segments):
            self.add_segments()
            self.body[n].goto(x=0 - 20 * n, y=0)
        self.screen.update()

    def level(self, difficulty):
        # todo 02: Snake's speed is modified as per the requested difficulty
        if difficulty == 1:
            self.speed = 0.08
            return self.speed
        elif difficulty == 2:
            self.speed = 0.05
            return self.speed
        elif difficulty == 3:
            self.speed = 0.02
            return self.speed

    # TODO 2: Move the snake
    def upwards(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def downwards(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def leftwards(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def rightwards(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        self.screen.listen()
        self.screen.onkeypress(fun=self.upwards, key='Up')
        self.screen.onkeypress(fun=self.downwards, key='Down')
        self.screen.onkeypress(fun=self.leftwards, key='Left')
        self.screen.onkeypress(fun=self.rightwards, key='Right')
        pole_position = (self.head.position())
        self.head.fd(20)

        for i in range(1, len(self.body)):
            trailing_position = self.body[i].position()
            self.body[i].goto(pole_position)
            pole_position = trailing_position
        self.screen.update()
        time.sleep(self.speed)
