import turtle
turtle.shape("turtle")

for i in range(3):
    turtle.goto(0,-50*i)
    turtle.down()
    turtle.forward(100)
    turtle.up()
    
turtle.done()