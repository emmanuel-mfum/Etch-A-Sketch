from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()


def move_forwards():  # function making the turtle go forwards
    timmy.forward(10)


def move_backwards():  # function making the turtle go backwards
    timmy.backward(10)


def counterclockwise():
    timmy.left(10)


def clockwise():
    timmy.right(10)


def clear():
    timmy.clear()  # clears the screen
    timmy.penup()  # the pen is now up
    timmy.home()  # makes the cursor returns to its initial location
    timmy.pendown()  # puts down the pen down


screen.listen()  # makes the screen listen to events

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counterclockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
