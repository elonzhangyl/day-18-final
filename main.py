import random

import colorgram
import turtle
import random

# Extract 6 colors from an image.
colors = colorgram.extract('hirst.jpeg', 20)
color_in_rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_in_rgb.append(new_color)
# print(color_in_rgb)

# print(colors)
tim = turtle.Turtle()
tim.hideturtle()
turtle.colormode(255)
r = 20
gap = 50
num_rows = 10
num_cols = 10
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.pendown()
tim.setheading(0)
for _ in range(num_rows):
    for _ in range(num_cols):
        tim.dot(r, random.choice(color_in_rgb))
        tim.penup()
        tim.forward(gap)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(gap)
    tim.left(90)
    tim.forward(gap * num_cols)
    tim.left(180)
    tim.pendown()

turtle.mainloop()