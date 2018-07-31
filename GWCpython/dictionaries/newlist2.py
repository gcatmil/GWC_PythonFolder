#Write a function that counts the frequency of each letter in a string

def letter_frequency(word):
#Dictionary holds count of each letter
#key = letter
#value = count
        frequency = {}

        for char in word:
                if char in frequency.keys():
                    frequency[char] = frequency[char] + 1
                #character isn't within the dictionary
                else:
                    frequency[char] = 1
        print(frequency)
letter_frequency("pen pineapple apple pen")
