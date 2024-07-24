from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_text.config(text="00:00")
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # # 1st 3ed 5th 7th rep:
    # if reps % 2 != 0:
    #     count_down(work_sec)
    # 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # 2nd 4th 6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# funciton 自己call 自己，相当于loop
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) # count-1是*arg,传递给count
    else:
        start_time()

        # if reps % 2 == 0 and reps > 0:
            # check_mark_1 = Label(text="✔", fg=GREEN,font=(FONT_NAME, 15, "bold"))
            # check_mark_1.grid(row=4, column=2, padx=shift)
            # shift +=5 🥵🥵🥵🥵🥵🥵只产生了一个√（原来思路是一个一个加√然后位移）， 解决思路是更新"✔"成为"✔✔"
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)



#
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=1, column=2)
# check mark
check_mark = Label(fg=GREEN,font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=4, column=2)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# highlightthickness=0 边缘的浅色圈去掉
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  #中心点
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2, column=2)



# button
start_button = Button(text="Start", font=("Arial", 12,), highlightthickness=0, command=start_time)
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", font=("Arial", 12,), highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=3)





window.mainloop()

# even driven 每毫秒检查一次，没有没有点屏幕，所以，上面有其他loop的时候回，就到不了mainloop