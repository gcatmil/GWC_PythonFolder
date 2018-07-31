#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ['Ysera', 'Alexstrasza', 'Kalec', 'Cyragosa', "Neltharion"]

#Generates a random integer.


ans = input('''Would you like a fun name? "yes" or "no"
''')
while ans != "no":
    if ans == "yes":
        aRandomIndex = randint(0, len(aList)-1)
        print(aList[aRandomIndex])
    else:
        print("{} is an invalid input.".format(ans))
    ans = input('''Would you like to roll again? "yes" or "no"]
    ''')
