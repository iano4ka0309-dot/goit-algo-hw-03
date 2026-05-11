import turtle

def koch(n, length):
    if n == 0:
        turtle.forward(length)
    else:
        koch(n-1, length/3)
        turtle.left(60)
        koch(n-1, length/3)
        turtle.right(120)
        koch(n-1, length/3)
        turtle.left(60)
        koch(n-1, length/3)

n = int(input("Введи рівень рекурсії: "))

turtle.hideturtle()
turtle.speed(0)

for i in range(3):
    koch(n, 300)
    turtle.right(120)

turtle.done()
