from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from random import choice, randint, shuffle
import pyperclip
import json

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)

reddish = "#d4483b"
bluish = "#1547a2"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
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
            new_data = {
                website_entry.get(): {
                    "email": email_entry.get(),
                    "password": password_entry.get()
                }
            }

            # Write data to json file
            # data_file = open("data.json", "w")
            # json.dump(new_data, data_file, indent=4)
            # data_file.close()

            # Read json file
            # data_file = open("data.json", "r")
            # data = json.load(data_file)
            # print(data)
            # data_file.close()

            # Update json file
            # If the json file is attempted to be updated while the file hasn't been created yet, the code
            # will throw an error (FileNotFound) hence the code to catch the error
            try:
                data_file = open("data.json", "r")
                # First, read old data
                data = json.load(data_file)
            except FileNotFoundError:
                data_file = open("data.json", "w")
                json.dump(new_data, data_file, indent=4)
                data_file.close()
            else:
                # Update old data with new data
                data.update(new_data)

                # Open data_file in write mode before saving updated data
                data_file = open("data.json", "w")
                # Save updated data
                json.dump(data, data_file, indent=4)
                data_file.close()

                print(data)
            finally:
                messagebox.showinfo(message="Data has been saved successfully.")

                website_entry.delete(0, END)
                website_entry.insert(0, "Website: ")

                email_entry.delete(0, END)
                email_entry.insert(0, "Email/Username: ")

                password_entry.delete(0, END)
                password_entry.insert(0, "Password: ")


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_data():
    website = website_entry.get()

    try:
        data_file = open("data.json", "r")
        data = json.load(data_file)
        data_file.close()

    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="Data not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            email_entry.delete(0, END)
            email_entry.insert(0, email)

            password_entry.delete(0, END)
            password_entry.insert(0, password)
        else:
            messagebox.showinfo(title="Oops!",
                                message="Website not found.,"
                                        f"\n\nNo details for {website} exists in the data file.")

    # try:
    #     website = data[website_entry.get()]
    #     print(website)
    # except KeyError:
    #     messagebox.showinfo(title="Oops!", message="Website not found.\n\nMake sure the website name is spelt correctly.")
    # else:
    #     email = website["email"]
    #     password = website["password"]
    #     data_file.close()
    #     email_entry.delete(0, END)
    #     email_entry.insert(0, email)
    #
    #     password_entry.delete(0, END)
    #     password_entry.insert(0, password)


# ---------------------------- COPY PASSWORD ------------------------- #
def copy_password():
    pyperclip.copy(password_entry.get())


# ---------------------------- UI SETUP ------------------------------- #
def clear_entry(event, entry):
    if entry.get() == "Website: " or entry.get() == "Email/Username: " or entry.get() == "Password: ":
        entry.delete(0, END)


window = Tk()
window.iconbitmap(default='favicon1.ico')
window.title("")
window.minsize(width=350, height=520)
window.config(padx=60, pady=40, bg="white")
window.resizable(False, False)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(row=0, column=0, columnspan=6)

style = ttk.Style(window)
style.theme_use('classic')
style.configure('SOExample.TEntry', relief='flat')
style.configure('My.TEntry', padding=(10, 7, 0, 7), relief="flat", borderwidth=0, focuscolor='#d4483b')
style.configure('My.TButton', padding=(5, 5, 0, 5), borderwidth=0, background="black", foreground="white",
                font=("Arial", 11))
style.map('My.TButton', background=[('active', "#424242")])
style.configure('TButton', padding=(6, 3, 6, 3), borderwidth=0, background=reddish, foreground="white",
                font=("Arial", 10))
style.map('TButton', background=[('active', reddish)], bordercolor=[('pressed', reddish)])


website_entry = ttk.Entry(window, style='My.TEntry', width=61, foreground="black", font=("Arial", 11))
website_entry.insert(0, "Website: ")
website_entry.grid(row=1, column=0, columnspan=6, pady=5)
website_entry.bind("<Button-1>", lambda event: clear_entry(event, website_entry))

email_entry = ttk.Entry(window, style='My.TEntry', width=61, foreground="black", font=("Arial", 11))
email_entry.insert(0, "Email/Username: ")
email_entry.grid(row=2, column=0, columnspan=6, pady=5)
email_entry.bind("<Button-1>", lambda event: clear_entry(event, email_entry))

password_entry = ttk.Entry(window, style='My.TEntry', width=52, foreground="black", font=("Arial", 11))
password_entry.insert(0, "Password: ")
password_entry.grid(row=3, column=0, columnspan=5, pady=5)
password_entry.bind("<Button-1>", lambda event: clear_entry(event, password_entry))

copy_password_btn = ttk.Button(window, style='TButton', text="Copy", width=7, command=copy_password)
copy_password_btn.grid(row=3, column=5)

gen_password_btn = ttk.Button(window, style='My.TButton', text="Generate Password", width=19, command=generate_password)
gen_password_btn.grid(row=4, column=0, columnspan=2, pady=4)

add_password_btn = ttk.Button(window, style='My.TButton', text="Save Password", width=19, command=save_data)
add_password_btn.grid(row=4, column=2, columnspan=2, pady=5)

search_password_btn = ttk.Button(window, style='My.TButton', text="Search Password", width=18, command=search_data)
search_password_btn.grid(row=4, column=4, columnspan=2, pady=5)

window.mainloop()
