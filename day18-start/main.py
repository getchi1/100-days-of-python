import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
#turtle starting from left
# timmy.penup()
# timmy.goto(-300, 0)
# timmy.pendown()

# timmy.color("VioletRed4")
timmy.speed("fastest")
#draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#draw dashed line
# for _ in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#draw all the shapes
# timmy.penup()
# timmy.goto(0, 300)
# timmy.pendown()
#
# colors = ["dark goldenrod", "dark olive green", "orchid", "chocolate", "dark orchid", "dark slate gray", "gold"]
# def draw_all_shapes(num_of_sides):
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#         timmy.right(angle)
#         timmy.forward(150)
# for fun_call in range(3, 11):
#     t_color = random.choice(colors)
#     timmy.color(t_color)
#     draw_all_shapes(fun_call)

#Random walk

# direction = [0, 90, 180, 270]
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# # colors = ["dark goldenrod", "dark olive green", "orchid", "chocolate", "dark orchid", "dark slate gray", "gold"]
# timmy.pensize(15)
# for _ in range(100):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(direction))
#     timmy.forward(50)

#Draw Spirograph

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#one way to the solution
# for _ in range(72):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(5)

#second way
def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()