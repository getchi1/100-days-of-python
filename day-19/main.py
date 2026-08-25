from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100]

all_turtles = []
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-370, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color} turtle is the winner")
            else:
                print(f"You lose! {winning_color} turtle is the winner")

        random_distance = random.randint(0, 100)
        turtle.forward(random_distance)


# def move_forward():
#     timmy.forward(10)
# def move_backward():
#     timmy.backward(10)
# def turn_left():
#     new_heading = timmy.heading() + 10
#     timmy.setheading(new_heading)
# def turn_right():
#     new_heading = timmy.heading() - 10
#     timmy.setheading(new_heading)
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()

