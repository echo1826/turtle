from turtle import Turtle, Screen
import turtle
import random

the_turtle = Turtle()
the_turtle.shape('turtle')
the_turtle.color('blue')
# draw a square
# for i in range(4):
#     the_turtle.forward(10)
#     the_turtle.right(90)

# draw dashed line
# for i in range(15):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()

# def draw_shape(num_side):
#     angle = CIRCLE / num_sides
#     for i in range(num_sides):
#         the_turtle.forward(100)
#         the_turtle.right(angle)        

colors = ["medium aquamarine", "gold", "red", "purple", "green", "blue", "black", "pink"]
# num_sides = 3
# CIRCLE = 360
# for j in range(3, 11):
#     the_turtle.color(random.choice(colors))
#     draw_shape(num_sides)
#     num_sides += 1

# draw a random walk
# directions = [0, 90, 180, 270]
# def walk(direction):
#     the_turtle.setheading(direction)
#     the_turtle.forward(30)

# turtle.colormode(255)
# def random_color():
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     return (red, green, blue)
# for i in range(250):
#     the_turtle.pensize(10)
#     the_turtle.speed(0)
#     the_turtle.color(random_color())
#     walk(random.choice(directions))

screen = Screen()
screen.exitonclick()