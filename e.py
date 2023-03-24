

# import turtle
import turtle
 
# initialising variables
dist = 1
flag = 200
 
# initialising turtle
spiral = turtle.Turtle()
 
# changing speed of turtle
spiral.speed(1000)
spiral.shapesize(1)
# making pattern
while flag:
   
    # makes the turtle to move forward
    spiral.forward(dist)
     
    # makes the turtle to move left
    spiral.left(100)
    spiral.left(20)
    dist += 1
    flag -= 1

turtle.update()
turtle.done()