# i = -1
# while True:
#     i += 1
#     if(i > 20):
#         break
#
#     if(i % 2 != 0):
#         continue
#     print(i)
# print("helllllllllllloooooooooooooooooooooooooo")

################################################

# number = 15
# tries = 0
#
# guess = int(input("What number is it? "))
# while tries < 3 and number != guess:
#     tries += 1
#     if number > guess:
#         guess = int(input("Guess higher: "))
#     else:
#         guess = int(input("Guess lower: "))
# print("The number is {}!".format(number))

number = 8
tries = 0

guess = int(input("whats the number? "))
for tries in range(3):
    if number > guess:
        guess = int(input("guess higher: "))
    elif number < guess:
        guess = int(input("guess lower: "))
    else:
        print("nope its {}".format(number))
    break

print("u right it is {}".format(number))


# print("congrats its {}")
