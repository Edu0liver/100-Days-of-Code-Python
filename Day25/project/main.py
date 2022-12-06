import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./Day25/project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./Day25/project/50_states.csv")
state_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]

        missing_states_csv = pandas.DataFrame(missing_states)
        missing_states_csv.to_csv("./Day25/project/missing_states.csv")
        
        break


    if answer_state in state_list:

        state_data = data[data.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

        guessed_states.append(state_data.state.item())
