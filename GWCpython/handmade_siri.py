########
# project beginning
########
def p1_greeting():
    print("Hello!\n To end chatting with this bot at any time, type 'end'")

def p2_greeting():
    print("Let us talk about your feelings :)")

def dating():
    print("I am 280 years, I am a Fashion Nova Instagram Model in my free time.\n During the day, I am normal boy chatbot. Just your regular, normal every day chatbot.\n But at night, I am Batman.")
    rep = input("soooo do u come here often?\n")
    print("interesting..??")

def advertisement():
    print("yeet my website is a file pathway on your computer!")
    rep2 = input("want to see it?\n")
    print("here it is! \nfile:///C:/Users/BlizzardGWC/Desktop/HTMLfuntimes/index.html")

def art():
    print('''
nnnn  nnnnnnnn       ooooooooooo        uuuuuu    uuuuuu
n:::nn::::::::nn   oo:::::::::::oo      u::::u    u::::u
n::::::::::::::nn o:::::::::::::::o     u::::u    u::::u
nn:::::::::::::::no:::::ooooo:::::o     u::::u    u::::u
  n:::::nnnn:::::no::::o     o::::o     u::::u    u::::u
  n::::n    n::::no::::o     o::::o     u::::u    u::::u
  n::::n    n::::no::::o     o::::o     u::::u    u::::u
  n::::n    n::::no::::o     o::::o     u:::::uuuu:::::u
  n::::n    n::::no:::::ooooo:::::o     u:::::::::::::::uu
  n::::n    n::::no:::::::::::::::o      u:::::::::::::::u
  n::::n    n::::n oo:::::::::::oo        uu::::::::uu:::u
  nnnnnn    nnnnnn   ooooooooooo            uuuuuuuu  uuuu
''')

def bad_day():
    print("not v good :(")

def nope():
        print("not really...\n....\nyouve made it awkwardly silent")

def is_valid_input(response, all_valid_input):
    if response in all_valid_input:
        return True
    else:
        return False


##############
# main functions
##############

def main():
    valid_input = ['hows life', 'doin good', 'you ok', 'show me art', 'draw something', 'doin good', 'you ok', 'end', 'art', 'do u have a website', 'AAAA', "hi!", 'Hello ;)', 'love me', 'come here often?', 'i need a partner in crime', 'are you my tinder date', 'how do it do', 'how do u do', 'scary', 'spooky', 'intimidating']
    p1_greeting()
    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer in ['Hello ;)', 'love me', 'come here often?', 'i need a partner in crime', 'are you my tinder date']:
                dating()

            elif answer in ['how do it do', 'how do u do']:
                bad_day()

            elif answer in ['scary', 'spooky', 'intimidating']:
                nope()

            elif answer == "hi":
                p2_greeting()

            elif answer == "end":
                break

            elif answer in ['art', 'show me art', 'draw something']:
                art()

            elif answer == "do u have a website":
                advertisement()

            elif answer in ['hows life', 'doin good', 'you ok']:
                print("I am doing okay!")

            elif answer == "AAAA":
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!\nwhy are we screaming?")
            else:
                print("pls")

        else:
            print("sorry! I cannot comprehend what you just said because it's not in the database of answers juuuuuussst yet :)\nhere are the responses I take:")
            for vi in valid_input:
                print(vi)
            print("....nothing else makes sense to me")

##############
# Don't touch!
##############
if __name__ == "__main__":
    main()
