import turtle
turtle.shape("turtle")

length=int(input("길이:"))
color=input("라인색:")
size=int(input("라인두께:"))

turtle.pencolor(color)
turtle.pensize(size)
turtle.forward(length)

turtle.done()