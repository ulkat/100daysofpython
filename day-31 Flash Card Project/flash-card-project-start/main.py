from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    list = data.to_dict(orient="records")
else:
    list = data.to_dict(orient="records")

def new_card_right():
    right()
    global current_card, flip_card
    window.after_cancel(flip_card)
    current_card = random.choice(list)
    canvas.itemconfig(card_img, image=card_front_image)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(word, fill="black")
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_card['French'])
    window.after(3000, card_back)


def new_card():
    global current_card, flip_card
    window.after_cancel(flip_card)
    current_card = random.choice(list)
    canvas.itemconfig(card_img, image=card_front_image)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(word, fill="black")
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_card['French'])
    window.after(3000, card_back)


def card_back():
    canvas.itemconfig(title, text="English", fill= "White")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=card_back_image)

def right():
    list.remove(current_card)
    unkown_words = pandas.DataFrame(list)
    unkown_words.to_csv("data/words_to_learn.csv", index=False)
    if list == [] :
        print("You know all the words")

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_card = window.after(3000, card_back)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, font=("ariel", 40, "italic"), text="Title")
word = canvas.create_text(400, 263, font=("ariel", 60, "bold"), text="word")
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=new_card_right)
button_right.grid(column=1, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=new_card)
button_wrong.grid(column=0, row=1)

new_card()


window.mainloop()
