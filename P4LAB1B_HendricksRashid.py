
#CTI-110
#P4HW2 - Initials
#Rashid Hendricks
#november 7, 2023
#

import turtle

t = turtle.Turtle()
t.penup()
# draw straight line
t.goto(-150, 50)
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(90)
t.forward(200)
t.backward(200)
t.left(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(100)
t.right(180)
t.forward(50)
t.right(70)
t.forward(128)

t = turtle.Turtle()
t.penup()
# draw straight line
t.goto(-10, 50) 
t.pendown()
t.pensize(10)
t.pencolor("blue")

t.right(90)
t.forward(200)
t.right(180)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(180)
t.forward(200)

turtle.done()
