import tkinter as tk
import json
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

    rand_password = [choice(letters) for _ in range(1, 5)]
    rand_password += [choice(numbers) for _ in range(1, 5)]
    rand_password += [choice(symbols) for _ in range(1, 5)]
    shuffle(rand_password)
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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # --- Message box --- #

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error!!!", message="Please fill all of the fields")
    else:
        # --- Save to txt --- #
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
                # Update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", "Invalid JSON in file: " + str(e))
            return
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))
            return

        try:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", "Failed to write to file: " + str(e))
            return

        # --- Wipe entry --- #
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    try:
        with open("data.json", "r") as file:
            website = website_entry.get()
            data = json.load(file)
            try:
                messagebox.showinfo(f"{website}", f" Email: {data[website]['email']} \n Password: {data[website]['password']}")
            except KeyError:
                messagebox.showinfo("Error", "No website found with this name")
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")

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
search_button = tk.Button(text="Search", command=search_password)

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
search_button.grid(column=2, row=1, sticky="EW")

# --- Default Email --- #
email_entry.insert(0, "testing@gmail.com")

# --- Focus --- #
website_entry.focus()

# -------- Main loop -------- #
window.mainloop()
