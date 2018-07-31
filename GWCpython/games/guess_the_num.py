import random
#TODO: define function guess_the_number
def guess_the_number():
    #use random.randint to get a number between 1 and 20
    n = random.randint(0, 20)
    #ask user to input their guess
    guess = int(input("Enter a random number!\n"))


    #TODO: loop to keep giving the player three guesses until they've guessed correctly
guess_the_number()
def main():
    while n != "guess":
        print
        if guess < n:
            print ("guess is low")
            guess = int(input("Enter a random number!\n"))
        elif guess > n:
            print( "guess is high")
            guess = int(input("Enter a random number!\n"))
        else:
            print("You got it!")
            break
        print

if __name__ == "__main__":
    main()
