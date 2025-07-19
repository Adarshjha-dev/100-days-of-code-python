from tkinter import *


def convert():
    m = float(miles_input.get())
    km = round(m * 1.609, 2)
    result.config(text=km)


window = Tk()
window.title("Miles to KM")
window.config(padx=40, pady=40)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
