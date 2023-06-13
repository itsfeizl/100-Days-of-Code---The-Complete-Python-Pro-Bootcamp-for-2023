from tkinter import *
import requests


def get_quote():
    # Write your code here.
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    kanye_quote_json = response.json()
    kanye_quote = kanye_quote_json["quote"] + "."
    canvas.itemconfig(quote_text, text=kanye_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click on Kanye to get a Kanye Quote", width=250, font=("Arial", 21, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, activebackground="#f0f0f0", borderwidth=0, relief='sunken',command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()