import turtle
import time

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
turtle.right(120)
turtle.forward(100)
turtle.right(120)

turtle.fillcolor("#0AEFDE")
turtle.begin_fill()

turtle.circle(100)
turtle.end_fill()

turtle.pencolor("#0AEFDE")
turtle.fillcolor("#FF0000")
turtle.begin_fill()
turtle.right(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

time.sleep(5)

