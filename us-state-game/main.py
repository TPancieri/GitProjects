import turtle as tl
import pandas as pd
# Display the US map on a screen
screen = tl.Screen()
screen.title("U.S. State Game")
screen.setup(width=725, height=491)
screen.bgpic("GitProjects/us-state-game/blank_states_img.gif")

states_guessed = 0

# Set up the state dict
df = pd.read_csv("GitProjects/us-state-game/50_states.csv")

# This sets the "state" column as the index of the DataFrame, then selects the "x" and "y" columns from the DF
# and finally converts the selected columns to a dictionary, using the index (i.e., the state names) as the keys.
state_values = df.set_index("state")[["x", "y"]].to_dict("index")

guessed_states = []

# While there's still blank states on the map, check input against the U.S. sate list
while states_guessed < 50:
    # Display an answer box for the user and take their input
    answer = screen.textinput(f"{states_guessed}/50 Guessed", "What's another state name?").title()
    # if the input is on the list , add it to the map
    if answer in state_values and answer not in guessed_states:
        state_x = state_values[answer]["x"]
        state_y = state_values[answer]["y"]
        new_state = tl.Turtle(visible=False)
        new_state.speed("fastest")
        new_state.color("black")
        new_state.penup()
        new_state.setpos(state_x, state_y)
        new_state.pendown()
        new_state.write(f"{answer}", align="center", font=('Arial', 10, 'bold'))
        screen.update()
        states_guessed += 1
        guessed_states.append(answer)
    if answer.lower() == "exit":
        missed_states = []
        for state in state_values:
            if state not in guessed_states:
                missed_states.append(state)
        
        
        missed_states_df = pd.DataFrame(missed_states)
        missed_states_df.to_csv("GitProjects/us-state-game/missed_states.csv")
        
        break
