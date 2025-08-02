import turtle

# Creating Canva
turtle.Screen().bgcolor("orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# Turtle Object Creation
board = turtle.Turtle()

# Creating a Square
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1

turtle.done()