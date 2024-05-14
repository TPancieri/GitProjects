import turtle as tl
import pandas as pd
# Display the US map on a screen
screen = tl.Screen()
screen.title("U.S. State Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

states_guessed = 0

# Display an answer box for the user
answer = screen.textinput(f"{states_guessed}/50 Guessed", "What's another state name?").lower()

# Take the user input and check it against the U.S. sate list
data = pd.read_csv("50_states.csv")
states = data["state"]
print(states)
# While there's still blank states on the map
if answer in states:
    print("Correct")

# if the input is on the list , add it to the map
# if not, try again
tl.mainloop()
