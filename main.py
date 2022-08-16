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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text="00:00")
    Label1.config(text="Timer")
    check_button.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        Label1.config("Break",fg=PINK)
        count_down(long_break_sec)

    elif reps%1 == 0:
        Label1.config(text="Work",fg=GREEN)
        count_down(work_sec)

    else:
        Label1.config("Break",fg=RED)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = count//60
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(timer_text,text =f"{count_min} : {count_sec}")
    if count>0:
       timer =  window.after(1000,count_down,count -1)
    else:
        start_timer()
        mark = ""
        work_session = reps//2
        for _ in range(work_session):
            mark += "✔"

        check_button.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")


Label1 = Label(text="Timer ")
Label1.config(fg=GREEN,font=(FONT_NAME,25,"bold"))
Label1.grid(column=1,row=1)


button1 = Button(text="start",highlightthickness=0,command=start_timer)
button1.grid(column=0,row=3)


button2 = Button(text = "reset",highlightthickness=0,command=reset_timer)
button2.grid(column=2,row=3)

check_state = IntVar()
check_button = Label(text="",fg=GREEN,bg=YELLOW)
check_button.grid(column=1,row=4)

window.config(padx=100,pady=35,bg=YELLOW)


canva = Canvas(width=200,height=200,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canva.create_image(100,85,image=image)
timer_text = canva.create_text(100,110,text="00:00",font=(FONT_NAME,25,"bold"))
canva.grid(column=1,row=2)




window.mainloop()