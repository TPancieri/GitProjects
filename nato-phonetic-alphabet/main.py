import pandas as pd

# Get the data
nato_data = pd.read_csv("GitProjects/nato-phonetic-alphabet/nato_phonetic_alphabet.csv")

# Create a dictionary:
nato_dict = {row.iloc[0]: row.iloc[1] for index, row in nato_data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please choose a word to be broken down to the nato phonetic alphabet \n").upper()
letter_list = [letter for letter in user_input]
phonetic = [nato_dict[letter] for letter in letter_list if letter in nato_dict]

# Print the phonetic code words
print("Phonetic code words:", ", ".join(phonetic))
