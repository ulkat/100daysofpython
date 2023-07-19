from tkinter import *

window = Tk()
window.title("Mile to Km")
window.minsize(width=300, height=200)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

convert_label = Label()
convert_label.grid(column=1, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)
def convert():
    km = round(int(entry.get())*1.6, 2)
    convert_label.config(text=str(km))

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)










window.mainloop()