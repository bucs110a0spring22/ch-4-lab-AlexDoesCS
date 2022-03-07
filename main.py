import turtle 
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
import math 

#Part A
wn = turtle.Screen()
fred = turtle.Turtle()

def drawSineCurve(fred):
  for xcor in range (-360, 361):
    ycor = math.sin(math.radians(xcor))
    fred.goto(xcor, ycor)
    fred.pendown()
  fred.penup()
fred.clear()
#Part B
def setupWindow(wn):
  wn.bgcolor('white')
  wn.setworldcoordinates(-360,-1,360,1)

def setupAxis(dart):
  dart.penup()
  dart.goto(-360,0)
  dart.pendown()
  dart.goto(360,0)
  dart.penup()
  dart.goto(0,-1)
  dart.pendown()
  dart.goto(0,1)
  dart.penup()
  dart.goto(0,0)

def drawCosineCurve(dart):
  for xcor in range(-360, 361):
    ycor = math.cos(math.radians(xcor))
    dart.goto(xcor, ycor)
    dart.pendown()
  dart.penup()
  
def drawTangentCurve(dart):
  for xcor in range(-360, 361):
    ycor = math.tan(math.radians(xcor))
    dart.goto(xcor, ycor)
    dart.pendown()
  dart.penup()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
