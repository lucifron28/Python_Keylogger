from tkinter import *
from tkmacosx import Button

expression = ""

def add_to_expression(symbol):
    global expression
    expression += str(symbol)
    text_result.config(state=NORMAL)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, expression, RIGHT)
    text_result.config(state=DISABLED)


def evaluate_expression():
    global expression
    text_result.config(state=NORMAL)
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    try:
        expression = str(eval(expression))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, expression, RIGHT)

    except Exception:
        clear_field()
        text_result.config(state=NORMAL)
        text_result.insert(1.0, "Error", RIGHT)
        text_result.config(state=DISABLED)
    finally:
        text_result.config(state=DISABLED)



def clear_field():
    global expression
    text_result.config(state=NORMAL)
    expression = ""
    text_result.delete(1.0, "end")
    text_result.config(state=DISABLED)


def delete_char():
    global expression
    text_result.config(state=NORMAL)
    expression = ""
    text_result.delete("end-2c", "end")
    text_result.config(state=DISABLED)

root = Tk()
root.geometry("360x380")
root.title("GUI Calculator")

text_result = Text(root, height=2, width=12, font=("Arial", 50), state="disabled", bg="white", fg="black")
text_result.grid(columnspan=50)
text_result.tag_configure("right", justify="right")



button_1 = Button(root, text="1", command=lambda: add_to_expression(1), width=90, height=50, font=("Arial", 28))
button_1.grid(row=2, column=1)

button_2 = Button(root, text="2", command=lambda: add_to_expression(2), width=90, height=50, font=("Arial", 28))
button_2.grid(row=2, column=2)

button_3 = Button(root, text="3 ", command=lambda: add_to_expression(3), width=90, height=50, font=("Arial", 28))
button_3.grid(row=2, column=3)

button_4 = Button(root, text="4", command=lambda: add_to_expression(4), width=90, height=50, font=("Arial", 28))
button_4.grid(row=3, column=1)

button_75 = Button(root, text="5", command=lambda: add_to_expression(5), width=90, height=50, font=("Arial", 28))
button_75.grid(row=3, column=2)

button_6 = Button(root, text="6", command=lambda: add_to_expression(6), width=90, height=50, font=("Arial", 28))
button_6.grid(row=3, column=3)

button_7 = Button(root, text="7", command=lambda: add_to_expression(7), width=90, height=50, font=("Arial", 28))
button_7.grid(row=4, column=1)

button_8 = Button(root, text="8", command=lambda: add_to_expression(8), width=90, height=50, font=("Arial", 28))
button_8.grid(row=4, column=2)

button_9 = Button(root, text="9", command=lambda: add_to_expression(9), width=90, height=50, font=("Arial", 28))
button_9.grid(row=4, column=3)

button_0 = Button(root, text="0", command=lambda: add_to_expression(0), width=90, height=50, font=("Arial", 28))
button_0.grid(row=5, column=2)

button_plus = Button(root, text="+", command=lambda: add_to_expression("+"), width=90, height=50, font=("Arial", 28), bg="orange")
button_plus.grid(row=2, column=4)

button_minus = Button(root, text="-", command=lambda: add_to_expression("-"), width=90, height=50, font=("Arial", 28), bg="orange")
button_minus.grid(row=3, column=4)

button_mul = Button(root, text="x", command=lambda: add_to_expression("x"), width=90, height=50, font=("Arial", 28), bg="orange")
button_mul.grid(row=4, column=4)

button_div = Button(root, text="÷", command=lambda: add_to_expression("÷"), width=90, height=50, font=("Arial", 28), bg="orange")
button_div.grid(row=5, column=4)

button_open_p = Button(root, text="(", command=lambda: add_to_expression("("), width=90, height=50, font=("Arial", 28))
button_open_p.grid(row=5, column=1)

button_close_p = Button(root, text=")", command=lambda: add_to_expression(")"), width=90, height=50, font=("Arial", 28))
button_close_p.grid(row=5, column=3)

button_equals = Button(root, text="=", command=evaluate_expression, width=90, height=50, font=("Arial", 28), bg="orange")
button_equals.grid(row=6, column=4)

button_clear = Button(root, text="Clear", command=clear_field, width=90, height=50, font=("Arial", 28), bg="orange")
button_clear.grid(row=6, column=2)

button_delete = Button(root, bg="orange", text="Del", command=delete_char, width=90, height=50, font=("Arial", 28), borderless=1)
button_delete.grid(row=6, column=3)


def key_equals(event):
    if event.keysym == "equal":
        button_equals.invoke()


root.bind("<KeyPress>", key_equals)

root.mainloop()