
# write a functon that prints a given dict in a sorted order (keys r sorted)

# Write a function, "pretty_print_dict" that prints a given dict in sorted order.
def pretty_print_dict(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

#Key = student name; value = disney character
students = {
"Annamarie" : "baymax",
"Adriana" : "rapunzel",
"Sydney" : "ariel",
"Lisette" : "mulan"
}

pretty_print_dict(students)

Mimi = {"height":"5 foot 4",
        "born":"Taiwan",
        "birthday":"Feburary 26"}
print(Mimi["born"])
