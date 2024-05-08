import turtle
'''
w = turtle.Screen()
w.title('Spiral Helix')
w.bgcolor('black')

colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow']

t = turtle.Pen()
t.speed(100)

for i in range(360):
    color = colors[i % len(colors)]
    t.pencolor(color)
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)
'''

turtle_screen = turtle.Screen()
turtle_screen.bgcolor('black')
turtle_screen.title('Spiral Helix')

turtle_instance = turtle.Turtle()
turtle_instance.color("light blue")
turtle_instance.speed(0)

for i in range(100):
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.done()