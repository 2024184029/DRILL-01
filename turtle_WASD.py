import turtle

turtle.pendown()
turtle.shape('turtle')
turtle.stamp()

def Up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def Down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def Left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.penup()
    turtle.clear()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.stamp()

turtle.listen()
turtle.onkey(Up, 'w')
turtle.onkey(Down, 's')
turtle.onkey(Left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(restart, 'Escape')

turtle.mainloop()
