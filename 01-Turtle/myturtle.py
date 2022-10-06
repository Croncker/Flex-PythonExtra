import turtle
import time

for x in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    
turtle.done()

venster = turtle.getscreen()
venster.bgcolor("black")

turtle.pencolor("#0AEFDE")
turtle.fillcolor("#FF0000")
turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

turtle.fillcolor("#0AEFDE")
turtle.begin_fill()

turtle.circle(100)
turtle.end_fill()
time.sleep(10)