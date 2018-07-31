import random
def evenorodd():
    computer_value = random.randint(0,10)
    print("{}".format(computer_value))
    user_input = input("Even or odd?\n")
    if ((computer_value%2) == 0) and (user_input == "even"):
        print("youre correct")
    elif ((computer_value%2) == 0) and (user_input == "odd"):
        print("no")
    elif ((computer_value%2) != 0) and (user_input == "even"):
        print("no")
    elif ((computer_value%2) != 0) and (user_input == "odd"):
        print("youre correct")
    else:
        print("wao")

evenorodd()
