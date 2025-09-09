import turtle

# 이 코드는 파이썬이 제공하는 tuple 기능을 이용한 것.
for x,y,r in [(200,200,50), (-200,-200,30), (100,100,50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write(str((x,y)))
