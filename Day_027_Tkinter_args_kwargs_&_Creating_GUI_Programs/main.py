import tkinter

# Create window
window = tkinter.Tk()

# Set window title
window.title("My first GUI program")

# Set window size
window.minsize(width=500, height=500)

# Set padding on window
window.config(padx=20, pady=20)


# Create a Button
def button_clicked():
    my_label["text"] = user_input.get()


# Create label
my_label = tkinter.Label(text="I am a label", font=("Arial", 16))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Alternative way of adding text to the label
# my_label["text"] = "New Text"


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button = tkinter.Button(text="Click Me Next", command=button_clicked)
button.grid(column=2, row=0)


# Create input textbox with the Entry() module
user_input = tkinter.Entry()
user_input.grid(column=3, row=2)

# Receive input text
user_input.get()


# Keep window open
window.mainloop()
