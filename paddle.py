from turtle import Turtle
#  The paddle should be 100 x 20 square.
STRETCH_WIDTH = 5
STRETCH_LENGTH = 1


#  Inherit from the Turtle class.
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    #  Using the self.forward() and self.setheading() here will make the object behave funny.
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
