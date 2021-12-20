from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=450, height=200)
window.config(padx=50, pady=50)

label_to_convert = Label(text="Miles")
label_to_convert.grid(row=3, column=3)

user_input = Entry(width=8)
user_input.grid(row=3, column=2)

print_out = Label(text="Equals")
print_out.grid(row=4, column=1)

converted_label = Label(text="Kilometers")
converted_label.grid(row=4, column=3)


def radio_used():
    if radio_state.get() == 1:
        label_to_convert.config(text="Miles")
        converted_label.config(text="Kilometers")
    if radio_state.get() == 2:
        label_to_convert.config(text="Kilometers")
        converted_label.config(text="Miles")


pick_label = Label(text="Measurment to Convert")
pick_label.grid(column=0, row=1)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Kilometers", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=2, column=0)
radiobutton2.grid(row=3, column=0)

converted_num = Label(text="0")
converted_num.grid(row=4, column=2)


def convert():
    if label_to_convert["text"] == "Miles":
        miles_to_convert = float(user_input.get())
        convert = round(miles_to_convert * 1.609344, 2)
        converted_num.config(text=str(convert))
    if label_to_convert["text"] == "Kilometers":
        km_to_convert = float(user_input.get())
        convert = round(km_to_convert * 0.6213712, 2)
        converted_num.config(text=str(convert))


calculate = Button(text="Convert!", command=convert)
calculate.grid(row=5, column=2)

window.mainloop()
