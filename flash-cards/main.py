import tkinter as tk
import pandas as pd
import random as rd


BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# --------------------- File Read ---------------------- #
with open("GitProjects/flash-cards/German-English.csv") as file:
    words_list = pd.read_csv(file)

german_list = words_list['German'].values.tolist()
english_list = words_list['English'].values.tolist()


# --------------------- Functions ---------------------- #
def choose_word():
    random_index = rd.randint(0, len(german_list) - 1)
    german_word = german_list[random_index]
    english_word = english_list[random_index]

    return german_word, english_word, random_index


def update_card():
    global german, english, word_index

    german, english, word_index = choose_word()
    canvas.itemconfig(title_tag, text="English")
    canvas.itemconfig(word_tag, text=english)
    root.after(3000, flip_card)


def flip_card():
    global german, english

    canvas.itemconfig(title_tag, text="German")
    canvas.itemconfig(word_tag, text=german)


def remove_card():
    global german_list, english_list, word_index

    german_list.pop(word_index)
    english_list.pop(word_index)

    update_card()


def next_card():
    update_card()


# ------------------------ UI ------------------------- #
# Window Setup
root = tk.Tk()
root.title("Flash Cards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Setup
canvas = tk.Canvas(width=800, height=526)
front_card = tk.PhotoImage(file="GitProjects/flash-cards/images/card_front.png")
canvas.create_image(400, 263, image=front_card)
title_tag = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_tag = canvas.create_text(400, 263, text="Title", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Button Setup
cross_image = tk.PhotoImage(file="GitProjects/flash-cards/images/wrong.png")
check_image = tk.PhotoImage(file="GitProjects/flash-cards\images/right.png")
cross_button = tk.Button(image=cross_image, border=0, highlightthickness=0, activebackground="red",
                        command=next_card)
checkmark_button = tk.Button(image=check_image, border=0, highlightthickness=0, activebackground="green",
                            command=remove_card)

# Positioning
canvas.grid(row=0, column=0, columnspan=2)
cross_button.grid(row=1, column=0)
checkmark_button.grid(row=1, column=1)

# ---------------------- Cards ------------------------ #
update_card()

# ----------------------- Root ------------------------ #
root.mainloop()
