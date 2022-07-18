# Messages in the program
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

# memory variable
memory = 0

# defining useful fuctions

# function for checking a integer is single digit or not
def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer() :
        return True
    else:
        return False

# function for checking easy calculations
def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    
    if msg != "":
        msg = msg_9 + msg
        print(msg)


# loop for continuos error checking
while True:
    print(msg_0)
    calc = input()
    oper_list = calc.split()
    operator = oper_list[1]
    x = oper_list[0]
    y = oper_list[2]

    # setting memory
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    # trying to convert strings into floats for calculation
    try:
        x = float(x)
        y = float(y)
    except:
        print(msg_1)
        continue  # repeat loop if error occured

    check(x, y, operator)  # checking and printing honest messages

    if (operator not in ["+", "-", "*", "/"]):
        print(msg_2)
        continue # repeat loop if error occured

    # if equation is correct
    if operator == "+":
        result = x + y
    elif operator == "*":
        result = x * y
    elif operator == "-":
        result = x - y
    elif operator == "/" and y == 0:
        print(msg_3)
        continue  # repeat loop if error occured by division by zero
    elif operator == "/" and y != 0:
        result = x / y

    print(result)  #printing result after successful calculation

    while True:  # loop for yes or no to store result in memory for after calculation
        print(msg_4)  # to store result in memory
        store_in_memory = input()

        if store_in_memory == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(eval('msg_' + str(msg_index)))
                    answer = input()

                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
            else:
                memory = result
            break
        elif store_in_memory == "n":
            break

    while True:  # to continue calculations
        print(msg_5)  
        continue_calculation = input()
        if continue_calculation == "n" or continue_calculation == "y":
            break;

    # continue calculation if answer was "y" for last msg_5
    if continue_calculation == "y":
        continue

    # successfully get out of loop and end program after calculations    
    break
