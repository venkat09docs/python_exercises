from turtle import Turtle, Screen

my_screen = Screen()
donatello = Turtle()

# Print the width of the canvas (in pixels)
print(my_screen.canvwidth)

# Set turtle shape and color
donatello.shape("turtle")  # Change shape to a turtle
donatello.color("purple")

# Move the turtle to draw
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(200)

# Return the turtle to its starting position
donatello.home()

# Create another turtle
raphael = Turtle()
raphael.color('red')  # Set color to red
raphael.shape('turtle')

# Move raphael to a new position without drawing
raphael.penup()
raphael.goto(-150, 200)
raphael.pendown()

# Draw circles using a loop
x = 10
while x <= 50:
    raphael.circle(x)
    donatello.circle(x + 5)
    x += 10

# Change pen color for drawing
raphael.pencolor('blue')




my_screen.exitonclick()