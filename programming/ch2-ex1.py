#simple first example to draw
#a flower with the turtle module
import turtle

#create window and turtle
window = turtle.Screen()
babbage = turtle.Turtle()
babbage.speed(10)

#draw stem
babbage.color("green", "black")
babbage.left(90)
babbage.forward(100)
babbage.right(90)

#draw the petals
for i in range(1,24):
    if babbage.color() == ("red", "red"):
        babbage.color("orange", "orange")
    elif babbage.color() == ("orange", "orange"):
        babbage.color("yellow", "yellow")
    else:
        babbage.color("red","red")

    babbage.begin_fill()
    babbage.left(15)
    babbage.forward(50)
    babbage.left(157)
    babbage.forward(50)
    babbage.end_fill()

#draw center
babbage.color("black", "black")
babbage.begin_fill()
babbage.circle(10)
babbage.end_fill()

#you already know
babbage.hideturtle()

#resolve window
window.exitonclick()
