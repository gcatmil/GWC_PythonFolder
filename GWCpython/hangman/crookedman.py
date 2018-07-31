#Have a word phrase
phrase = "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
#Keep track of user's guesses
guessed_letters = []
game_over = False

#Tell user how many spaces and letters
display = ""
for letter in phrase:
    if letter in guessed_letters:
        display += letter
    elif letter == " ":
        display += " "
    #the letter in our phrase has not been guessed yet
    else:
        display += "_ "
print(display)

while game_over != True:
    #Allow user to give input to computer
    guess = input("Enter a letter: ")

    #Tell the user if they get the right letter
        #Add the good letter to our good letter list
    if guess in phrase:
        print("You got a letter: {}".format(guess))

    #Tell the user if they get the wrong letter
        #Add the bad letter to our bad letter list
    else:
        print("{} is not in the phrase".format(guess))

    #Add the guess letter to our list of guessed letters
    guessed_letters.append(guess)

    display = ""
    for letter in phrase:
        if letter in guessed_letters:
            display += letter
        elif letter == " ":
            display += " "
        #the letter in our phrase has not been guessed yet
        else:
            display += "_ "
    print(display)

    # game_over = True
    total_underscore = 0
    for d in display:
        #There's an underscore, so the game is not over.
        if d == "_":
            # game_over = False
            total_underscore += 1
    if total_underscore == 0:
        game_over = True
    else:
        game_over = False
#End the game if the user gets all the right letters in our word phrase
print("u r donezo!!")
