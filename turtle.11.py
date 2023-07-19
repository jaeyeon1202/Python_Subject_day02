import turtle
turtle.shape("turtle")

dis=int(input("거리:"))
line=input("라인색:")
fill=input("거북이 색:")
size=int(input("라인두께:"))

turtle.fillcolor(fill)
turtle.pencolor(line)
turtle.pensize(size)

for i in range(3):
    turtle.forward(dis)
    turtle.right(90)
# turtle.forward(dis)
# turtle.right(90)
#turtle.forward(dis)

turtle.done()