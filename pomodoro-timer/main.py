import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    cycles_label.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Long Rest", fg=RED)
        count_down(LONG_BREAK_MIN* 60)
    elif reps % 2 == 0:
        title_label.config(text="Short Rest", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work")
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        # waits 1000 ms and call a function
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        cycles_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)

title_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=2, row=1)

canvas = tk.Canvas(width=300, height=330, bg=YELLOW, highlightthickness=0)
pomodoro_image = tk.PhotoImage(file="GitProjects/pomodoro-timer/tomato.png")
canvas.create_image(150, 165, image=pomodoro_image)
timer_text = canvas.create_text(150, 185, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = tk.Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.place(x=100, y=150)
start_button.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.place(x=250, y=100)
reset_button.grid(column=3, row=3)


cycles_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
cycles_label.grid(column=2, row=4)

window.mainloop()
