from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from random import choice, randint, shuffle
import pyperclip
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)

reddish = "#d4483b"
bluish = "#1547a2"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 16))]
    password_list += [choice(symbols) for _ in range(randint(4, 8))]
    password_list += [choice(numbers) for _ in range(randint(4, 8))]
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if website_entry.get == "Website" or email_entry.get() == "Email/Username":
        messagebox.showinfo(title="Oops!", message="Invalid website name or email/username.")
    elif website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Oops!", message="Text fields cannot be empty!")
    else:
        is_ok = messagebox.askokcancel(
            message=f"Website: {website_entry.get()}\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\n\nSave data?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(
                "{'website': '" + website_entry.get() + "', 'email': '" + email_entry.get() + "', 'password': '" + password_entry.get() + "'}" + "\n")
            f.close()

            # upload_file_list = ['data.txt']
            # for upload_file in upload_file_list:
            #     gfile = drive.CreateFile({'parents': [{'id': '1hHi77k_zBgXhrcINV9I1L-Ct3LcdeZuG'}]})
            #     # Read file and set it as the content of this instance.
            #     gfile.SetContentFile(upload_file)
            #     gfile.Upload()  # Upload the file.

            messagebox.showinfo(message="Data has been saved successfully.")

            website_entry.delete(0, END)
            website_entry.insert(0, "Website")

            email_entry.delete(0, END)
            email_entry.insert(0, "Email/Username")

            password_entry.delete(0, END)
            password_entry.insert(0, "Password")


# ---------------------------- UI SETUP ------------------------------- #
def clear_entry(event, entry):
    if entry.get() == "Website" or entry.get == "Email/Username" or entry.get() == "Password":
        entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.minsize(width=350, height=480)
window.config(padx=60, pady=40, bg="white")
window.resizable(False, False)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

style = ttk.Style(window)
style.theme_use('classic')
style.configure('SOExample.TEntry', relief='flat')
style.configure('My.TEntry', padding=(10, 7, 0, 7), relief="flat", borderwidth=0, focuscolor='#d4483b')
style.configure('My.TButton', padding=(5, 5, 0, 5), borderwidth=0, background="black", foreground="white",
                font=("Arial", 11))
style.map('My.TButton', background=[('active', "#424242")])

website_entry = ttk.Entry(window, style='My.TEntry', width=50, foreground="black", font=("Arial", 11))
website_entry.insert(0, "Website")
website_entry.grid(row=1, column=0, columnspan=2, pady=5)
website_entry.bind("<Button-1>", lambda event: clear_entry(event, website_entry))

email_entry = ttk.Entry(window, style='My.TEntry', width=50, foreground="black", font=("Arial", 11))
email_entry.insert(0, "Email/Username")
email_entry.grid(row=2, column=0, columnspan=2, pady=5)
email_entry.bind("<Button-1>", lambda event: clear_entry(event, email_entry))

password_entry = ttk.Entry(window, style='My.TEntry', width=50, foreground="black", font=("Arial", 11))
password_entry.insert(0, "Password")
password_entry.grid(row=3, column=0, columnspan=2, pady=5)
password_entry.bind("<Button-1>", lambda event: clear_entry(event, password_entry))

gen_password_btn = ttk.Button(window, style='My.TButton', text="Generate Password", width=23, command=generate_password)
gen_password_btn.grid(row=4, column=0, pady=5)
# gen_password_btn.place(x=0, y=335)

add_password_btn = ttk.Button(window, style='My.TButton', text="Add Password", width=24, command=save_data)
add_password_btn.grid(row=4, column=1, pady=5)
# add_password_btn.place(x=211, y=335)

window.mainloop()
