import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. state game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State correct",
                                    prompt="What's another state name").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        # state_to_learn.csv this file will contain the states which are not guessed
        new_data.to_csv("state_to_learn.csv")
        break
    #If answer_state is present in the list of 50_state.csv
    if answer_state in all_states:
        guess_state.append(answer_state)
        #if true
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        t.goto(state_data.x.item(), state_data.y.item())
        t.color("black")
        t.write(state_data.state.item())


