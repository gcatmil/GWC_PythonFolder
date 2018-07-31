#define function madlibs
def madlibs():
    print("Please enter a verb: ")
    c_input = input()

    print("Please enter a noun: ")
    y_input = input()

    print("Please enter a (pro)noun: ")
    z_input = input()

#gather the input

madlibs()
#TODO: output the finished madlib with the inputs you received

story = "Britty was blank to school one day.\n She was trying to get a blank2 from the store before heading to class. \nUnfortunately, blank3 blocked her."

for word in story_list:
    # the word is a shorthand
    if word in sl_terms.keys():
        new_story_list.append(sl_terms[word])
        # the word is not a shorthand
    else:
        new_story_list.append(story)
print(new_story_list)
print(" ".join(new_story_list))
