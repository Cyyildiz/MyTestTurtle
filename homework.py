import turtle
import time

windows = turtle.Screen()
windows.tracer(0)

player = turtle.Turtle()
timer_text = turtle.Turtle()

start = time.time()

while time.time() - start < 21:
    player.forward(1)
    player.left(1)
    timer_text.clear()
    timer_text.write(int(time.time() - start), font=("botton", 20))
    
    windows.update()
turtle.write("Game Over", font=("Verdana", 15, "top"))
turtle.done()


