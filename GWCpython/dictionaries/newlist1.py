# aaaa

def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

sl_terms = {"omg":"oh my gawd",
            "l8r":"later",
            "ttyl":"talk to you later",
            "gn":"good night",
            "gg":"good game",
            "w/e":"whatever",
            "wow":"world of warcraft",
            "lol":"league of legends",
            "b&":"banned",
            "smh":"shaking my head",
            "imo":"in my opinion",
            "gwcsip":"girls who code summer immersion program"}

translate_shorthand(sl_terms)

story = """
Stacy was texting . She said lol noobs suck smh . imo wow is better .
are you going to gwcsip ?
"""

story_list = story.split()
new_story_list = []

# go through each word of our story
for word in story_list:
    # the word is a shorthand
    if word in sl_terms.keys():
        new_story_list.append(sl_terms[word])
        # the word is not a shorthand
    else:
        new_story_list.append(story)
print(new_story_list)
print(" ".join(new_story_list))
