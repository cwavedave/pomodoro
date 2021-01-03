import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_engage():
    countdown(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,countdown,count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Application")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME, 35,"bold"))

canvas.grid(column=1,row=2)

title = Label(text="Timer", font=("Arial",36,"bold"), bg=YELLOW, fg=RED)
title.grid(column=1,row=1)

button_start = Button(text="Start",command=timer_engage)
button_start.grid(column=0,row=3)

button_reset = Button(text="Reset")
button_reset.grid(column=3,row=3)

label_tick = Label(text="✅",bg=YELLOW)
label_tick.grid(column=1,row=4)

window.mainloop()

