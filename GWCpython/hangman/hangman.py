def print_beginning_of_game():
    print("HANGMAN BEGINS")
def display(word, already_guessed_letters ):
    str1 = ""
    for letter in word:
        if letter in already_guessed_letters:
            str1 += letter
        elif letter == " ":
            str1 += " "
        #the letter in our phrase has not been guessed yet
        else:
            str1 += "_ "
    # print(str1)
    return str1

#Have a word phrase
def main():
    phrase = "youd better believe it"
    #Keep track of user's guesses
    guessed_letters = []
    game_over = False

    #Tell user how many spaces and letters
    sturt = display(phrase, guessed_letters)
    print(sturt)

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

        goodmorning = display(phrase, guessed_letters)
        print(goodmorning)

        # game_over = True
        total_underscore = 0
        for d in goodmorning:
            #There's an underscore, so the game is not over.
            if d == "_":
                # game_over = False
                total_underscore += 1
        if total_underscore == 0:
            game_over = True
        else:
            game_over = False
#End the game if the user gets all the right letters in our word phrase
    print("t. naruto")
if __name__ == "__main__":
    main()
