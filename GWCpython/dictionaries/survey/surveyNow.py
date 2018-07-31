import json
import os

def surveyStart():
    print("Hello!")
    intA = input("What is your name? ")
    if intA == str(intA):
        print("Welcome " + str(intA) + " to my survey!")
        print("We will be continuing to ask you 8 questions:")
    else:
        pass

questionsDict = {
'meme' : "what is the meme u think about most? ",
'emote' : "what is your favorite emote face (like ;3)? ",
'dessert' : "what is your favorite dessert food? ",
'flavor' : "whats ur favorite flavor? ",
'perfume' : "whats ur favorite perfume? ",
'sbux' : "what is ur faVorite starbuckz drink? ",
'animal' : "what is ur favorite animal? "}
twoPointOh = []

information = True
while information == True:
    surveyStart()
    response = {}
    for category, question in questionsDict.items():
        response[category] = input(question)
    intB = input("would u like 2 continue? (yes/no) ")
    twoPointOh.append(response)
    if intB == "yes" or intB == "Yes" or intB == "Ye" or intB == "ye":
        information = True
    else:
        print("kbye")
        information = False
## this would go here but like it dont work
        # if os.path.isfile("surveyNow.json"):
        #     file = open("surveyNow.json", "r+")
        #     old_data = json.load(file)
        #     file.write(json.dumps(old_data))
        #     file.close()
        # else:
        #     file = open("data.json", "w")
        #     file.write(json.dumps(data))
        #     file.close

f = open("surveyNow.json", "w")
jsonStuff = json.dumps(response)
f.write(jsonStuff)
f.close()
