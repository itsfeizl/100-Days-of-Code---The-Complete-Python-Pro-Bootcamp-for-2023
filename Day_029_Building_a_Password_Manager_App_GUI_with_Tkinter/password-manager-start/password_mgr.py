from tkinter import *
import tkinter.ttk as ttk

reddish = "#d4483b"
bluish = "#1547a2"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=350, height=480)
window.config(padx=60, pady=40, bg="white")
window.resizable(False, False)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=0, row=0)

style = ttk.Style(window)
style.theme_use('classic')
style.configure('SOExample.TEntry', relief='flat')
style.configure('My.TEntry', padding=(10, 7, 0, 7), relief="flat", borderwidth=0, focuscolor='#d4483b')
style.configure('My.TButton', padding=(5, 5, 0, 5), borderwidth=0, background="black", foreground="white", font=("Arial", 11))
style.map('My.TButton', background=[('active', "#424242")])

website_label = Label()

title_label = Label(font=("Arial", 11), bg="white")
title_label.config(text="Website")
title_label.place(x=10, y=190)

website_entry = ttk.Entry(window, style='My.TEntry', width=51, foreground="grey", font=("Arial", 11))
website_entry.grid(column=0, row=1, pady=20)


email_label = Label(font=("Arial", 11), bg="white")
email_label.config(text="Email/Username")
email_label.place(x=10, y=270)

email_entry = ttk.Entry(window, style='My.TEntry', width=51, foreground="grey", font=("Arial", 11))
email_entry.grid(column=0, row=2, pady=20)

# email_entry = ttk.Entry(window, style='My.TEntry', width=51, foreground="grey", font=("Arial", 11))
# email_entry.insert(0, "Email/Username")
# email_entry.grid(column=0, row=2, pady=5)

# password_entry = ttk.Entry(window, style='My.TEntry', width=51, foreground="grey", font=("Arial", 11))
# password_entry.insert(0, "Password")
# password_entry.grid(column=0, row=3, pady=5)
# password_entry.bind("<Button-1>", lambda event: clear_entry(event, password_entry))
#
# gen_password_btn = ttk.Button(window, style='My.TButton', text="Generate Password", width=24)
# gen_password_btn.place(x=0, y=335)
#
# add_password_btn = ttk.Button(window, style='My.TButton', text="Add Password", width=24)
# add_password_btn.place(x=211, y=335)

window.mainloop()
