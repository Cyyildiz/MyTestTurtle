import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.up(100)
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(90)
turtle_instance_2.forward(100)

turtle_instance_3 = turtle.Turtle(100)
turtle_instance_3.right(90)
turtle_instance_3.forward(100)
'''
'''----------------------------------------------------------------
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
'''
'''
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
'''

#star
'''----------------------------------------------------------------
turtle_instance = turtle.Turtle()
turtle_instance.left(45)
turtle_instance.forward(100)
turtle_instance.left(-90)
turtle_instance.forward(100)
turtle_instance.left(135)
turtle_instance.forward(100)
turtle_instance.left(-45)
turtle_instance.forward(100)
turtle_instance.left(135)
turtle_instance.forward(100)
turtle_instance.left(315)
turtle_instance.forward(100)

turtle_instance.left(135)
turtle_instance.forward(100)

turtle_instance.left(-90)
turtle_instance.forward(100)

turtle_instance.left(135)
turtle_instance.forward(100)

turtle_instance.left(-45)
turtle_instance.forward(100)
'''
'''
turtle_instance.left(-45)
turtle_instance.forward(100)
'''
'''
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(100)
'''
turtle_instance = turtle.Turtle()
num_sides = 6
angle =360.0 / 6
side_length = 100
for i in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)

turtle.done()