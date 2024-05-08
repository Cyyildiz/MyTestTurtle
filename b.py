# import package 
from turtle import *
from time import sleep
turtle = Turtle()
screen = Screen()
screen.onscreenclick(turtle.goto)
turtle.getscreen()._root.mainloop()

# method to action 
def fxn(x,y): 
	
	# some motion 
	turtle.right(90) 
	turtle.forward(100) 

# turtle speed to slowest 
turtle.speed(1) 

# motion 
turtle.fd(100) 

# allow user to click 
# for some action 
turtle.onclick(fxn)
