# Draw a Koch snowflake
from turtle import *
import turtle

# from Jeff. A.
# fig 1.3 #1
def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(t)
    else:
        forward(a)

# custom hexagon von-koch like fractal
def hexagon(a, order):
    if order > 0:
        for t in [120, -60, -60, -60, -60, 120, 0]:
            hexagon(a/7, order-1)
            #forward(a)
            left(t)
    else:
        forward(a)


# custom heptagon von-koch like fractal
def heptagon(a, order):
    if order > 0:
        for t in [128.6, -51.43, -51.43, -51.43, -51.43, -51.43, 128.6, 0]:
            heptagon(a/7, order-1)
            #forward(a)
            left(t)
    else:
        forward(a)

# closed heptagon von-koch like fractal
# produces a flower shape
# uninteresting, produces the same order 2 pattern over and over again because of it being closed
def closed_heptagon(a, order):
    if order > 0:
        for t in [-51.43, -51.43, -51.43, -51.43, -51.43, -51.43, -51.43]:
            closed_heptagon(a/7, order-1)
            #forward(a)
            left(t)
    else:
        forward(a)

# fig 1.3 #2
def n8r14(a, order):
    if order > 0:
        for t in [ 90, -90, -90, 0, 90, 90, -90, 0]:
            n8r14(a/4, order-1)
            #forward(a)
            left(t)
    else:
        forward(a)

# fig 1.3 #3
def n9r13(t, a, order):
    if order > 0:
        n9r13(t, a/3, order-1)
        # Save current position and direction
        position = t.position()
        heading = t.heading()

        # Left branch
        t.left(90)
        n9r13(t, a/3, order-1)
        t.left(-90)
        n9r13(t,a/3, order-1)
        t.left(-90)
        n9r13(t,a/3, order-1)
        t.left(-90)
        n9r13(t,a/3, order-1)

        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()
        t.left(-90)
        n9r13(t,a/3, order-1)
        t.left(90)
        n9r13(t,a/3, order-1)
        t.left(90)
        n9r13(t,a/3, order-1)
        t.left(-90)
        n9r13(t,a/3, order-1)

    else:
        t.forward(a)


# custom cross-like fractal
def cross(t, a, order):
    if order > 0:
        t.left(-90)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)

        # Save current position and direction
        position = t.position()
        heading = t.heading()

        # Left branch
        t.left(90)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)

        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()
        t.left(-90)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)
        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)
        n9r13(t, a/3, order-1)



    else:
        t.forward(a)

# Test
#koch(100, 0)
# Choose colours and size
#color("white")
#bgcolor("black")
#screen = turtle.Screen()
size = 3333
order = 3
# Ensure snowflake is centred
# penup()
# backward(size/1.732)
# left(30)
# pendown()

# Make it fast
tracer(100)
hideturtle()

#begin_fill()
t = turtle.Turtle()
#n9r13(t,size, order)
#cross(t, size, order)
#closed_heptagon(size, order)
hexagon(size, order)
#end_fill()
# Make the last parts appear
update()
done()