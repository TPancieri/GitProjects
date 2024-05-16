import tkinter as tk

# Constants
MILES_TO_KM_CONVERSION_FACTOR = 1.609344


def convert():
    """Convert miles to kilometers"""
    try:
        miles = int(entry.get())
        result = miles * MILES_TO_KM_CONVERSION_FACTOR
        value_label.config(text=f"{result:.2f}")
    except ValueError:
        value_label.config(text="Invalid input")


window = tk.Tk()
window.title("Miles to Km")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

# Create the entry field
entry = tk.Entry(width=15)
entry.grid(column=2, row=1)

# Create the labels
miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=1)

equal_label = tk.Label(text="Is equal to")
equal_label.grid(column=1, row=2)

value_label = tk.Label(text="0")
value_label.grid(column=2, row=2)

kilometer_label = tk.Label(text="Kilometer")
kilometer_label.grid(column=3, row=2)

# Create the button
button = tk.Button(text="Calculate", command=convert)
button.grid(column=2, row=3)

# Start the main loop
window.mainloop()
