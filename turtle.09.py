import turtle
turtle.shape("turtle")

side=int(input("한 변의 길이:"))
color=input("라인색:")
size=int(input("라인두께:"))

turtle.pencolor(color)
turtle.pensize(size)

for i in range(3):
    turtle.forward(side)
    turtle.left(120)

turtle.done()