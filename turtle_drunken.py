import turtle
import random

turtle.shape('turtle')
while(True):
    turtle.setheading(random.randint(0, 30)) # 30도 각도 내에서 다음 이동?
    turtle.forward(random.randint(100, 200))
    turtle.stamp()