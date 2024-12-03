import turtle
import time

# Set up the turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(5)
t.color("purple")

# Move to starting position
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw 'h'
t.left(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)

# Move to position for 'a'
t.penup()
t.goto(-120, 0)
t.pendown()

# Draw 'a'
t.left(180)
t.forward(100)
t.right(180)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Move to position for 'f'
t.penup()
t.goto(-40, 0)
t.left(90)
t.pendown()

# Draw 'f'
t.forward(100)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
t.backward(50)
t.right(90)
t.forward(40)

# Move to position for 's'
t.penup()
t.goto(40, 100)
t.pendown()

# Draw 's'
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Move to position for 'a'
t.penup()
t.goto(120, 0)
t.left(90)
t.pendown()

# Draw final 'a'
t.forward(100)
t.right(180)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Hide turtle and keep window open
t.hideturtle()
turtle.done() 