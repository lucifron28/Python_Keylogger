from tkinter import *

def add():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        answer_label["text"] = "Sum: "
        answer_text.config(state=NORMAL)
        answer_text.delete(1.0, END)
        answer_text.insert(END, x + y)
        answer_text.config(state=DISABLED)
    except ValueError as e:
        print(e)

def subtract():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        answer_label["text"] = "Difference: "
        answer_text.config(state=NORMAL)
        answer_text.delete(1.0, END)
        answer_text.insert(END, x - y)
        answer_text.config(state=DISABLED)
    except ValueError as e:
        print(e)

def multiply():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        answer_label["text"] = "Product: "
        answer_text.config(state=NORMAL)
        answer_text.delete(1.0, END)
        answer_text.insert(END, x * y)
        answer_text.config(state=DISABLED)
    except ValueError as e:
        print(e)

def divide():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        answer_label["text"] = "Quotient: "
        answer_text.config(state=NORMAL)
        answer_text.delete(1.0, END)
        answer_text.insert(END, x / y)
        answer_text.config(state=DISABLED)
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

def modulus():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        answer_label["text"] = "Modulus: "
        answer_text.config(state=NORMAL)
        answer_text.delete(1.0, END)
        answer_text.insert(END, x % y)
        answer_text.config(state=DISABLED)
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

window = Tk()
window.geometry("500x350")
window.title("Simple Calculator: Ron Vincent Cada")
window.configure(padx="30px", pady="50px")
input_frames = Frame(window)
input_frames.grid(row=1, column=1, columnspan=5, sticky="ew", pady="5px", padx="25px")
label_x = Label(input_frames, text="1st Number:", font=("Arial", 20, "bold"), fg="#E92F2F")
label_x.grid(row=1, column=1)

label_y = Label(input_frames, text="2nd Number:", font=("Arial", 20, "bold"), fg="#426EEC")
label_y.grid(row=2, column=1)

entry_x = Entry(input_frames, font=("Arial", 20))
entry_x.grid(row=1, column=2)

entry_y = Entry(input_frames, font=("Arial", 20))
entry_y.grid(row=2, column=2)

button_frame = Frame(window)
button_frame.grid(row=2, column=1, columnspan=5, sticky="ew", pady="5px", padx="30px")

add_button = Button(button_frame, text="Add", width="3", height="1", command=add, font=("Arial", 15, "bold"))
add_button.grid(row=3, column=1)

subtract_button = Button(button_frame, text="Subtract", width="4", height="1", command=subtract, font=("Arial", 15, "bold"))
subtract_button.grid(row=3, column=2)

multiply_button = Button(button_frame, text="Multiply", width="4", height="1", command=multiply, font=("Arial", 15, "bold"))
multiply_button.grid(row=3, column=3)

divide_button = Button(button_frame, text="Divide", width="4", height="1", command=divide, font=("Arial", 15, "bold"))
divide_button.grid(row=3, column=4)

modulus_button = Button(button_frame, text="Modulus", width="4", height="1", command=modulus, font=("Arial", 15, "bold"))
modulus_button.grid(row=3, column=5)

answer_frame = Frame(window)
answer_frame.grid(row=4, column=1, columnspan=5, pady="5px", padx="10px")
answer_label = Label(answer_frame, text="Answer:", font=("Arial", 20, "bold"), fg="green")
answer_label.grid(row=1, column=1)

answer_text = Text(answer_frame, height=1, width=20, font=("Arial", 20), state=DISABLED)
answer_text.grid(row=1, column=2)
window.mainloop()