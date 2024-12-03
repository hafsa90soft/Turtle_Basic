import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(2)
t.pensize(5)

# Move to starting position
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw H
t.left(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.backward(100)

# Move to position for A
t.penup()
t.right(90)
t.forward(30)
t.pendown()

# Draw A
t.left(70)
t.forward(110)
t.right(140)
t.forward(110)
t.backward(55)
t.right(110)
t.forward(37)

# Move to position for F
t.penup()
t.left(180)
t.forward(37)
t.right(110)
t.forward(55)
t.right(70)
t.forward(30)
t.pendown()

# Draw F
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(30)

# Move to position for S
t.penup()
t.forward(30)
t.pendown()

# Draw S
t.forward(50)
t.backward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Move to position for A
t.penup()
t.left(180)
t.forward(80)
t.pendown()

# Draw final A
t.left(70)
t.forward(110)
t.right(140)
t.forward(110)
t.backward(55)
t.right(110)
t.forward(37)

# Hide turtle and display
t.hideturtle()
turtle.done()
