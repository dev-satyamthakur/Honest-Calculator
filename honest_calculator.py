# Messages in the program
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"

# memory variable
memory = 0

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
    elif y == "M":
        y = memory

    # trying to convert strings into floats for calculation
    try:
        x = float(x)
        y = float(y)
    except:
        print(msg_1)
        continue  # repeat loop if error occured

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
