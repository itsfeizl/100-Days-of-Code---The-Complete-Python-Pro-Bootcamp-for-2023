from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=220)
window.config(padx=20, pady=20)

welcome_label = Label(font=("Arial", 12))
welcome_label.config(text="Welcome to the miles to km converter.")
welcome_label.place(x=20, y=0)

direction_label = Label(font=("Arial", 12))
direction_label.config(text="Enter number and hit 'Calculate' to convert.")
direction_label.place(x=5, y=20)

user_input = Entry(font=("arial", 12))
user_input.insert(0, "0")
user_input.place(x=75, y=60, width=50, height=30)

style = Style()
style.configure('TButton', font=('Arial', 12, 'bold'), borderwidth='5')


def calculate():
    user_entry = user_input.get()
    num_in_km = round(int(user_entry) * 1.609)
    answer_label.config(text=f"{user_entry} miles converted to km is {num_in_km}")


calc_button = Button(text="Calculate", command=calculate)
calc_button.place(x=130, y=59, width=100, height=32)

canvas = Canvas()
canvas.create_line(50, 25, 250, 25)
canvas.place(x=0, y=90)

answer_label = Label(font=("Arial", 14, "bold"), anchor="e", justify=LEFT)
answer_label.config(text=f"0 miles converted to km is 0")
answer_label.place(x=155, y=130, anchor="n")


window.mainloop()
