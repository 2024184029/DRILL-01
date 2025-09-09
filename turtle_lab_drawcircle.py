import turtle

def drawCircle(x, y, r):
    turtle.penup()
    turtle.goto(x, y)
    turtle.stamp()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)


turtle.shape('turtle')
drawCircle(0,0,50)
drawCircle(200,200,100)
drawCircle(100,-100,50)