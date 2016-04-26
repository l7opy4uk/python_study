"""
calc function used for basic calculations
"""
user_input_a = None
def calc():
    user_input_a = 0
    set_defaults()
    last_dig = 0
    VALID_CHR = ["+", "-", "*", "/", "exit", "=", "_", "help", "c"]
    print_greetings(VALID_CHR)
    # Cheking for digits in first number
    user_input_a = int_check(user_input_a, "first?")
    write_file(user_input_a)
    while True:
        ## We are cheking for invalid char's in operant.
        user_input_op = valid_check(VALID_CHR)
        if user_input_op != "exit" or user_input_op != "help":
            write_file(user_input_op)
        if user_input_op == "=":
                print(user_input_a)
        elif user_input_op == "help":
            print("List of available actions: ")
            print(VALID_CHR)
        elif user_input_op == "c":
            set_defaults()
            print(user_input_a)
            user_input_a = int_check(user_input_a, "first?")
        else:
            ## Takes input from user for new number, if operant == "_" - it's return
            ## previous number that was input by user.
            user_input_b = last_num(last_dig)
            last_dig = user_input_b
            user_input_a = op_processing(user_input_a, user_input_b, user_input_op)

#def check_operant_global():

def set_defaults():
    global user_input_a, user_input_b
    user_input_a = 0
    user_input_b = 0


def print_greetings(VALID_CHR):
    print("\nGreetings on Python-calc!"
          "\nClosed Alpha test"
          "\nSoftware version: 0.0.5"
          "\n\nList of available actions(print in 'op?'): ")
    print(VALID_CHR)

def sum_(x, y):
    return x + y
def diff_(x, y):
    return x - y
def mult_(x, y):
    return x * y
def separ_(x, y):
    return x / y

def last_num(last_dig):
    ## Takes input from user for new number, if operant == "_" - it's return
    ## previous number that was input by user.
    while True:
        x = input("dig?")
        write_file(x)
        if x == "_":
            x = last_dig
            return x
        else:
            try:
                x = int(x)
                return x
            except ValueError:
                print("You need to use digits")
                continue

def valid_check(l):
    ## We are cheking for invalid char's in operant.
    while True:
        x = input("op?")
        count = 0
        for i in l:
           if x == i:
               return x
           else:
               count += 1
               if count > len(l) - 1:
                   print("Invalid character")

def int_check(x, y = ""):
    ## Cheking for digits in first number
    while True:
        try:
            return int(input(y))
        except ValueError:
            print("You need to use numbers")

def op_processing(user_input_a, user_input_b, user_input_op):
    ## Function fo operant checking
    while True:

        if user_input_op == "+":
            user_input_a = sum_(user_input_a, user_input_b)
        elif user_input_op == "-":
            user_input_a = diff_(user_input_a, user_input_b)
        elif user_input_op == "*":
            user_input_a = mult_(user_input_a, user_input_b)
        ## Cheking for ZeroDevision error
        elif user_input_op == "/":
            if user_input_b == 0:
                print("ZeroDivision:")
            else:
                user_input_a = separ_(user_input_a, user_input_b)
        elif user_input_op == "exit":
            exit()
        return user_input_a

def write_file(l):
    with open("write.txt", "a") as f:
        f.write(str(l))
calc()
