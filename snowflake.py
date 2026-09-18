# Draw a Koch snowflake
from turtle import *
import turtle

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(t)
    else:
        forward(a)

def hexagon(a, order):
    if order > 0:
        for t in [120, -60, -60, -60, -60, 120, 0]:
            hexagon(a/7, order-1)
            #forward(a)
            left(t)
    else:
        forward(a)


# Test
#koch(100, 0)
# Choose colours and size
#color("white")
#bgcolor("black")
#screen = turtle.Screen()
size = 77777
order = 7
# Ensure snowflake is centred
# penup()
# backward(size/1.732)
# left(30)
# pendown()

# Make it fast
tracer(100)
hideturtle()

#begin_fill()

# Three Koch curves
hexagon(size, order)

#end_fill()
# Make the last parts appear
update()
done()