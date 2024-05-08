from turtle import Screen, Turtle


def show_money():
    player.clear()
    player.forward(20)
    player.pendown()
    player.write(f"Money: {money}", font=("monospace", 16))
    player.penup()
    player.backward(20)


def add_money(x, y):
    global money
    money += 1
    show_money()
    Screen().update()


money = 0
Screen().tracer(0)
player = Turtle()
player.color("green")
player.shape("circle")
player.showturtle()
player.penup()
player.turtlesize(1.2, 1.2)
player.onclick(add_money)
show_money()
Screen().update()
Screen().mainloop()