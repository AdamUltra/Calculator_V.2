from tkinter import *
import math
POSSIBLE_OPERATORS = ("+", "-", "÷", "×", "*", "/")
POSSIBLE_NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".")
win = Tk()
win.config(pady=20, padx=20)
win.geometry("220x255")
win.title("Calculator")
result = ""
special = ""
special_num = ""
equation_in_system = ""
expression_in_output = ""
insert_oper = True


def calculate(equation):
    global result, equation_in_system, special, special_num
    special_num = ""
    try:
        for num in equation:

            special = equation[equation.index(num):equation.index(")") + 1]
            for i in special:
                if i in POSSIBLE_NUMBERS:
                    special_num += i

            if num == "c":
                special_num = str(math.cos(int(special_num)))

            elif num == "s":
                special_num = str(math.sin(int(special_num)))

            elif num == "t":
                special_num = str(math.tan(int(special_num)))

            equation = equation.replace(special, special_num)
            equation_in_system = equation

    except ValueError:
        pass

    result = eval(f"{equation}")
    output.config(text=f"{result}")


def update_output():
    output.config(text=f"{expression_in_output}")


def add_number(num):
    global expression_in_output, POSSIBLE_OPERATORS, insert_oper, equation_in_system
    insert_oper = True
    if num in POSSIBLE_OPERATORS:
        if expression_in_output[-1] in POSSIBLE_OPERATORS:
            insert_oper = False

        else:
            insert_oper = True

    if insert_oper:
        if num == "*":
            expression_in_output += "×"

        elif num == "//":
            expression_in_output += "÷"

        else:
            expression_in_output += num
        equation_in_system += num
    update_output()


def back_space():
    global expression_in_output, equation_in_system
    expression_in_output = expression_in_output[:len(expression_in_output) - 1]
    equation_in_system = equation_in_system[:len(equation_in_system) - 1]
    update_output()


def ac():
    global expression_in_output, equation_in_system
    expression_in_output = ''
    equation_in_system = ''
    update_output()


output = Label(text="", height=2, width=23, anchor=SE, bg="grey")
output.grid(column=0, row=1, columnspan=500)

equal_button = Button(text="=", width=4, height=5, command=lambda: calculate(equation_in_system), border=0)
equal_button.grid(column=4, row=5, rowspan=2)
ac_button = Button(text="AC", width=4, height=2, command=ac, border=0)
ac_button.grid(column=1, row=2)
divide_button = Button(text="÷", width=4, height=2, command=lambda: add_number("//"), border=0)
divide_button.grid(column=2, row=2)
mult_button = Button(text="×", width=4, height=2, command=lambda: add_number("*"), border=0)
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
decimal_button = Button(text=".", width=4, height=2, command=lambda: add_number("."), border=0)
decimal_button.grid(column=3, row=6)
percent_button = Button(text="%", width=4, height=2, command=lambda: add_number("%"), border=0)
percent_button.grid(column=1, row=6)
brackets_button = Button(text=")", width=4, height=2, command=lambda: add_number(")"), border=0)
brackets_button.grid(column=5, row=2)
cos_button = Button(text="cos", width=4, height=2, command=lambda: add_number("cos("), border=0)
cos_button.grid(column=5, row=3)
sin_button = Button(text="sin", width=4, height=2, command=lambda: add_number("sin("), border=0)
sin_button.grid(column=5, row=4)
tan_button = Button(text="tan", width=4, height=2, command=lambda: add_number("tan("), border=0)
tan_button.grid(column=5, row=5)
win.mainloop()
