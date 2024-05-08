from turtle import Screen, Turtle

written = 0

def click(x, y):
    global written

    written += 1
    pen.clear()
    pen.write(written, align='center')

screen = Screen()
screen.setup()
screen.title("Button Counting")
screen.bgcolor('red')

button = Turtle()
button.shape("square")
button.shapesize(10)
button.goto(10,40)
button.color("white")
button.onclick(click)

pen = Turtle()
pen.hideturtle()
pen.write(written, align='center')

screen.mainloop()