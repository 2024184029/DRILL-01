import turtle

while True:
    shape = input('Enter shape: ')
    if shape == 'circle':
        turtle.circle(50)
    elif shape == 'triangle':
        turtle.forward(50); turtle.left(120)
        turtle.forward(50); turtle.left(120)
        turtle.forward(50)
    elif shape == 'quit':
        break
    else:
        print('Wrong shape')

turtle.bye() # 왜 실행 안 됨?