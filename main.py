import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    label_tick.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_engage():
    global reps
    reps += 1
    print(reps)
    if reps % 8 == 0:
        title.config(text="Long Break",fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title.config(text="Short Break",fg=YELLOW)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        title.config(text="Work Time",fg=GREEN)
        countdown(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,countdown,count - 1)
    else:
        timer_engage()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✅"
        label_tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Application")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1,row=2)

title = Label(text="Timer", font=("Arial",36,"bold"), bg=YELLOW, fg=RED)
title.grid(column=1,row=1)

button_start = Button(text="Start",command=timer_engage)
button_start.grid(column=0,row=3)

button_reset = Button(text="Reset",command=reset_timer)
button_reset.grid(column=3,row=3)

label_tick = Label(text="",bg=YELLOW)
label_tick.grid(column=1,row=4)

window.mainloop()