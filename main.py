from tkinter import *
POSSIBLE_OPERATORS = ("+", "-", "÷", "×")
POSSIBLE_NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
win = Tk()
win.config(pady=20, padx=20)
win.geometry("190x255")
win.title("Calculator")
nums = ""
oper = ""
result = ""
expression = ""
insert_oper = True
cont_ins = True


def calculate(equation):
    global nums, result, oper
    result = 0
    nums = ""
    oper = ""
    for i in equation:
        if i in POSSIBLE_NUMBERS:
            nums += i

        else:

            if len(oper) == 0:
                result = int(nums)
            oper = i
            nums = ""

        if len(oper) >= 1 and len(nums) >= 1:
            if oper == "+":
                result += int(nums)

            elif oper == "-":
                result -= int(nums)

            elif oper == "×":
                result *= int(nums)

            elif oper == "÷":
                result //= int(nums)

    output.config(text=f"{result}")


def update_output():
    output.config(text=f"{expression}")


def add_number(num):
    global expression, POSSIBLE_OPERATORS, insert_oper
    insert_oper = True
    if num in POSSIBLE_OPERATORS:
        if expression[-1] in POSSIBLE_OPERATORS:
            insert_oper = False

        else:
            insert_oper = True
    if insert_oper:
        expression += num
    update_output()


def back_space():
    global expression
    expression = expression[:len(expression)-1]
    update_output()


def ac():
    global expression
    expression = ''
    update_output()


# logo = Label(text="CALCULATOR", font=("courier", 20, "bold"))
# logo.grid(column=0, row=0, columnspan=100)
output = Label(text="", height=2, width=20, anchor=SE, bg="grey")
output.grid(column=0, row=1, columnspan=500)

# extra = Label(text='', width=4, height=2)
# extra.grid(column=0, row=0)
equal_button = Button(text="=", width=4, height=5, command=lambda: calculate(expression), border=0)
equal_button.grid(column=4, row=5, rowspan=2)
ac_button = Button(text="AC", width=4, height=2, command=ac, border=0)
ac_button.grid(column=1, row=2)
divide_button = Button(text="÷", width=4, height=2, command=lambda: add_number("÷"), border=0)
divide_button.grid(column=2, row=2)
mult_button = Button(text="×", width=4, height=2, command=lambda: add_number("×"), border=0)
mult_button.grid(column=3, row=2)
subtract_button = Button(text="-", width=4, height=2, command=lambda: add_number("-"), border=0)
subtract_button.grid(column=4, row=3)
add_button = Button(text="+", width=4, height=2, command=lambda: add_number("+"), border=0)
add_button.grid(column=4, row=4)
bksp_button = Button(text="Bksp", width=4, height=2, command=back_space, border=0)
bksp_button.grid(column=4, row=2)
seven_button = Button(text="7", width=4, height=2, command=lambda: add_number("7"), border=0)
seven_button.grid(column=1, row=3)
eight_button = Button(text="8", width=4, height=2, command=lambda: add_number("8"), border=0)
eight_button.grid(column=2, row=3)
nine_button = Button(text="9", width=4, height=2, command=lambda: add_number("9"), border=0)
nine_button.grid(column=3, row=3)
six_button = Button(text="6", width=4, height=2, command=lambda: add_number("6"), border=0)
six_button.grid(column=3, row=4)
five_button = Button(text="5", width=4, height=2, command=lambda: add_number("5"), border=0)
five_button.grid(column=2, row=4)
four_button = Button(text="4", width=4, height=2, command=lambda: add_number("4"), border=0)
four_button.grid(column=1, row=4)
three_button = Button(text="3", width=4, height=2, command=lambda: add_number("3"), border=0)
three_button.grid(column=3, row=5)
two_button = Button(text="2", width=4, height=2, command=lambda: add_number("2"), border=0)
two_button.grid(column=2, row=5)
one_button = Button(text="1", width=4, height=2, command=lambda: add_number("1"), border=0)
one_button.grid(column=1, row=5)
zero_button = Button(text="0", width=4, height=2, command=lambda: add_number("0"), border=0)
zero_button.grid(column=2, row=6)

win.mainloop()