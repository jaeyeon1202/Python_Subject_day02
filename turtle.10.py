import turtle
turtle.shape("turtle")

for i in range(6):
    turtle.forward(100)
    turtle.right(30)
    turtle.backward(100)
    turtle.right(30)

turtle.up()
turtle.goto(150,0)
turtle.down()

for i in range(4):
    turtle.forward(100)
    turtle.right(45)
    turtle.backward(100)
    turtle.right(45)

turtle.up()
turtle.goto(-150,0)
turtle.down()

for i in range(3):
    turtle.forward(100)
    turtle.right(36)
    turtle.backward(100)
    turtle.right(36)

turtle.done()