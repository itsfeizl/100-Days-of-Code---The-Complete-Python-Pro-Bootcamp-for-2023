from tkinter import *
import pandas
import random
from tkinter import messagebox

fr_words_to_learn_dict = {}
ENGLISH = "English"
FRENCH = "French"


def remove_word():
    try:
        fr_words_list.remove(random_fr_word)
        fr_words_to_learn_list = fr_words_list.copy()
        en_for_words_to_learn_list = [data_dict[item] for item in fr_words_to_learn_list]

        fr_words_to_learn_dict[FRENCH] = fr_words_to_learn_list
        fr_words_to_learn_dict[ENGLISH] = en_for_words_to_learn_list

        df = pandas.DataFrame(fr_words_to_learn_dict)
        df.to_csv("data/words_to_learn.csv", index=False)
    except ValueError:
        messagebox.showinfo(title="Notice",
                            message="There are no more words left that you don't know.\nCongratulations!")
    # if not fr_words_list:
    #     messagebox.showinfo(title="Notice", message="There are no more words left that you don't know.\nCongratulations!")

    change_words()


def gen_random_num():
    try:
        return random.randint(0, len(fr_words_list) - 1)
    except ValueError:
        print("No more French words to learn.")


def flip_cards():
    try:
        canvas.itemconfig(fr_word, text=data_dict[random_fr_word], fill="white")
    except KeyError:
        pass
    else:
        canvas.itemconfig(language, text=ENGLISH, fill="white")
        canvas.itemconfig(card_bg, image=bg_back_img)


def change_words():
    global flip_timer
    window.after_cancel(flip_timer)
    try:
        changed_fr_word = fr_words_list[gen_random_num()]
        canvas.itemconfig(fr_word, text=changed_fr_word, fill="black")
        global random_fr_word
        random_fr_word = changed_fr_word
    except TypeError:
        canvas.itemconfig(language, text="Hooray!", fill="black")
        canvas.itemconfig(fr_word, text="Congrats", fill="black")
        canvas.create_text(400, 340, text="You've learnt all the words in these cards.", fill="black", font=("Arial", 14))
        window.after_cancel(flip_timer)
    else:
        canvas.itemconfig(language, text=FRENCH, fill="black")
        canvas.itemconfig(card_bg, image=bg_front_img)

        flip_timer = window.after(3000, flip_cards)


# Get data from csv file
# First try to open words_to_learn.csv. If the file is not found, then open french_words.csv
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


# Convert csv data to Python dictionary
data_dict = {value[FRENCH]: value[ENGLISH] for (key, value) in data.iterrows()}
# data_dict = {"f_name": "Faisal", "l_name": "Hassan", "age": 36, "profession": "Developer"}
fr_words_list = [key for key in data_dict]


# Set up window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg="#b1ddc6")
window.resizable(False, False)  # Prevents window from resizing


# Set timer: Invoke the function flip_cards after 3000 ms
flip_timer = window.after(3000, flip_cards)

try:
    random_fr_word = fr_words_list[gen_random_num()]
except TypeError:
    print("No more French words to learn.")
    FRENCH = "Hooray!"
    random_fr_word = "Congrats"
    window.after_cancel(flip_timer)


# Save images from local folder into variables
bg_front_img = PhotoImage(file="images/card_front.png")
bg_back_img = PhotoImage(file="images/card_back.png")


# Create canvas of width and height dimensions of 800px and 526px respectively
# Set the canvas up with a background color of #b1ddc6 and highlight thickness of 0
canvas = Canvas(width=800, height=526)
canvas.config(bg="#b1ddc6", highlightthickness=0)


# Set up image saved in bg_front_img variable as canvas background
card_bg = canvas.create_image(400, 263, image=bg_front_img)


# Create texts "French" and word stored in the variable random_fr_word on canvas
language = canvas.create_text(400, 150, text=FRENCH, fill="black", font=("Arial", 35, "italic"))
fr_word = canvas.create_text(400, 253, text=random_fr_word, fill="black", font=("Arial", 82, "bold"))


# Set up canvas position on window; positioned on row 0, column 0, and spans into column 1
canvas.grid(column=0, row=0, columnspan=2)


# Set up buttons. Buttons backgrounds will be images

# First, store images from local folder into variables
wrong_btn_img = PhotoImage(file="images/wrong.png")
right_btn_img = PhotoImage(file="images/right.png")


# Create wrong button
# Same background color as active background (activebackground="#b1ddc6") and sunken relief removes animation on button
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, activebackground="#b1ddc6", relief='sunken',
                   borderwidth=0, bg="#b1ddc6", command=change_words)

# Define wrong button position on window
wrong_btn.grid(column=0, row=1, padx=50, pady=20)

# Create right button
right_btn = Button(image=right_btn_img, highlightthickness=0, activebackground="#b1ddc6", relief='sunken',
                   borderwidth=0, bg="#b1ddc6", command=remove_word)

# Define right button position on window
right_btn.grid(column=1, row=1, padx=50, pady=20)


# Keep window open until user closes it
window.mainloop()
