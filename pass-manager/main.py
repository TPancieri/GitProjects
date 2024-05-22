import tkinter as tk
from tkinter import messagebox
from random import choice, shuffle
from pyperclip import copy


# ---------------------------- WARNING  ----------------------------#
# THIS STORES PASSWORDS IN PLAIN TEXT, IT WAS DONE ONLY FOR LEARNING
# DO NOT ACTUALLY USE THIS TO STORE ANY PASSWORD, IT IS NOT SAFE!!!

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    password_entry.delete(0, tk.END)

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ",", ".", "<",
            ">", "/", "?", "~"]

    # --- Adding chars --- #

    # Generate 4 random letters
    rand_password = [choice(letters) for _ in range(1, 5)]

    # Generate 4 random numbers
    rand_password += [choice(numbers) for _ in range(1, 5)]

    # Generate 4 random symbols
    rand_password += [choice(symbols) for _ in range(1, 5)]

    # --- Shuffles password --- #
    shuffle(rand_password)

    # --- Converts the list to a string --- #
    password_str = "".join(rand_password)

    # --- Inserts password into entry --- #
    password_entry.insert(0, password_str)

    # --- Copy to clipboard --- #
    copy(password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # --- Message box --- #

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error!!!", message="Please fill all of the fields")

    else:
        confirmed = messagebox.askokcancel(title=website, message=f"Are these details correct?  "
                                                                f"\n Email: {email}, \n Password: {password}")

        if confirmed:
            # --- Save to txt --- #
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")

            # --- Wipe entry --- #
            website_entry.delete(0, tk.END)
            # email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("MyPass")
window.resizable(width=False, height=False)
window.config(pady=50, padx=50)

# --- Logo --- #
logo = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="logo.png")
logo.create_image(100, 100, image=lock_image)

# --- Labels --- #
website_label = tk.Label(text="Website: ", font=("", 10, ""))
email_label = tk.Label(text="Email/Username: ", font=("", 10, ""))
password_label = tk.Label(text="Password: ", font=("", 10, ""))

# --- Entry --- #
website_entry = tk.Entry(width=35)
email_entry = tk.Entry(width=35)
password_entry = tk.Entry(width=21)

# --- Buttons --- #
generate_button = tk.Button(text="Generate Password", command=generate_password)
add_button = tk.Button(text="Add", width=36, command=save_password)

# -------- Grid positions -------- #

# --- Logo --- #
logo.grid(column=1, row=0)

# --- Website --- #
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# --- Email --- #
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# --- Password --- #
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)

# --- Buttons --- #
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# --- Default Email --- #
email_entry.insert(0, "testing@gmail.com")

# --- Focus --- #
website_entry.focus()

# -------- Main loop -------- #
window.mainloop()
