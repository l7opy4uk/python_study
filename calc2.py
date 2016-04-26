"""
calc function used for basic calculations
"""

def calc():
    stop = False
    user_input_a = 0
    user_input_b = 0
    user_input_op = ""
    while True:
        try:
            user_input_a = int(input("Put your number:\n"))
            break
        except ValueError:
            print("You need to use numbers")
            continue
    while True:
        try:
            user_input_op = input()

        except ValueError:
            print("You need to input numbers")
        else:
            if user_input_op == "+":
                user_input_b = int_check(user_input_b)
                user_input_a = sum_(user_input_a, user_input_b)
            elif user_input_op == "-":
                user_input_b = int_check(user_input_b)
                user_input_a = diff_(user_input_a, user_input_b)
            elif user_input_op == "*":
                user_input_b = int_check(user_input_b)
                user_input_a = mult_(user_input_a, user_input_b)
            elif user_input_op == "/":
                user_input_b = int_check(user_input_b)
                user_input_a = separ_(user_input_a, user_input_b)
            elif user_input_op == "=":
                print(user_input_a)
            elif user_input_op == "exit":
                exit()
            else:
                print("Incorrect operant")
                continue




def sum_(x, y):
    return x + y
def diff_(x, y):
    return x - y
def mult_(x, y):
    return x * y
def separ_(x, y):
    return x / y

def int_check(x, y = ""):
    while True:
        try:
            x = int(input(y))
        except ValueError:
            print("You need to use numbers")
        else:
            return x

calc()
