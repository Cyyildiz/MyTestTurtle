import turtle
import time

my_screen = turtle.Screen()
my_screen.title("Clicker Game")
my_screen.bgcolor("light green")

score = 0

def display_score():
    score_pen.clear()
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.goto(0, 260)
    score_pen.write("Score: {}".format(score), align="center", font = ("Courier",24, "normal"))

def click(x,y):
    global score
    score += 1
    display_score()

def countdown():
    timer_pen = turtle.Turtle()
    timer_pen.speed(0)
    timer_pen.color("black")
    for i in range(20, 1, -1):
        time.sleep(1)
        timer_pen.clear()
        timer_pen.penup()
        timer_pen.hideturtle()
        timer_pen.goto(0, 220)
        timer_pen.write("Time Left: {}".format(i), align="center", font=("Courier", 24, "normal"))
        my_screen.update()
    my_screen.bye()

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")

def start_game(x, y):
    my_screen.onclick(click)
    countdown()

display_score()

my_screen.onclick(start_game)

my_screen.mainloop()