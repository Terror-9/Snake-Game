from turtle import Turtle, Screen

screen = Screen()
leo = Turtle("turtle")

def move_forward():
    leo.forward(20)

# Press the "w" key to move the turtle forward
screen.listen()
screen.onkeypress(move_forward, "w")

screen.exitonclick()