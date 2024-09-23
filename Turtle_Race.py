import turtle
import time
import random
#Variables
Create_Screen=turtle.Screen
Player=turtle.Turtle()
speeed=5
comp=turtle.Turtle()
#Code
comp.setheading(90)
comp.penup()
comp.setx(30)
comp.pendown()
Player.setheading(90)
def PlayerMove():
    Player.setheading(90)
    Player.forward(5)
turtle.listen()
turtle.onkey(PlayerMove,"w")
while True:
    comp.forward(5)
    time.sleep(random.randrange(0,3))
turtle.done()