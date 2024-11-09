from turtle import Turtle, Screen


sai = Turtle()
sai.shape("turtle")


def move_forwards():
    sai.forward(10)

def move_backwards():
    sai.backward(10)

# def counter_clockwise():
#     sai.left(10)
# both works the same
def counter_clockwise():
    new_heading = sai.heading() + 10
    sai.setheading(new_heading)


def clockwise():
    sai.right(10)

def clear_drawing():
    sai.clear()
    sai.penup()
    sai.home()
    sai.pendown()

screen = Screen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen = Screen()
screen.listen()
screen.exitonclick()

