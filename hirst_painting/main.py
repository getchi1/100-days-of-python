# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     rgb = color.rgb
#     rgb_colors.append((rgb.r, rgb.g, rgb.b))
#
# print(rgb_colors)
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("arrow")
timmy.speed("fastest")
t.colormode(255)

color_list = [(228, 247, 239), (248, 230, 240), (206, 160, 107), (218, 232, 243), (128, 166, 191), (54, 106, 138), (196, 141, 162), (128, 180, 157), (226, 202, 117), (140, 70, 93), (152, 84, 57), (45, 124, 96), (168, 156, 53), (188, 91, 115), (201, 95, 74), (230, 167, 187), (70, 160, 131), (60, 156, 174), (14, 98, 74), (120, 36, 56), (160, 210, 190), (22, 48, 74), (234, 172, 161), (113, 118, 162), (69, 28, 46), (182, 184, 217), (42, 56, 102), (18, 58, 42), (69, 36, 22)]
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300) #arrow moves by 50 paces so 50*6(dots)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(15, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()