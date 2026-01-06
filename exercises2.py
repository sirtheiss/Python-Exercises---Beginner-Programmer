#IN THESE EXERCISES, I STARTED LEARNING TEXT MANIPULATION
# Exercises Table starting from 22
from os import name

print("=== Exercises Menu ===")
print("22 - Uppercase and Lowercase")
print("23 - Thousands, hundreds, tens and units")
print("231 - Thousands, hundreds, tens and units")
print("24 - City name contains 'Saint'")
print("25 - Does the name contain 'Silva'?")
print("26 - Sentence, count letter A")
print("27 - First and last name")

ex = int(input("Type the number of the exercise you want to execute: "))

# Exercise 22 - OK
if ex == 22:
    full_name = input("Type your full name: ").strip()
    print("Your name is {}".format(full_name.upper()))
    print("Your name is {}".format(full_name.lower()))
    print("Your name has {} letters in total".format(len(full_name) - full_name.count(" ")))
    print("Your first name has {} letters".format(len(full_name.split()[0])))

# Exercise 23 - OK
if ex == 23:
    n = input("Type a number from 1 to 9999: ")
    num = str(n)
    if len(num) >= 5:
        print("Invalid number!")
    else:
        print(
            "Your number has {} units,\n {} tens,\n {} hundreds\n and {} thousands".format(
                num[3], num[2], num[1], num[0]
            )
        )

# Exercise 23.1 - OK
if ex == 231:
    n = int(input("Type a number from 1 to 9999: "))
    thousands = n // 1000
    hundreds = n % 1000 // 100
    tens = n % 100 // 10
    units = n % 10
    print(
        "Your number has {} thousand(s), {} hundred(s), {} ten(s) and {} unit(s)".format(
            thousands, hundreds, tens, units
        )
    )

# Exercise 24 - OK
if ex == 24:
    city_name = input("Type the name of your city: ")
    city_title = city_name.title()
    city_title.find("Saint")
    if city_title.find("Saint") == -1:
        print('Your city does not have "Saint" in its name')
    else:
        print('Your city has "Saint" in its name')

# Exercise 25 - OK
if ex == 25:
    full_name = input("Type your full name: ")
    name_title = full_name.title()
    name_title.find("Silva")
    if name_title.find("Silva") == -1:
        print("You do not have Silva in your name")
    else:
        print("You have Silva in your name")

# Exercise 26 - OK
if ex == 26:
    sentence = input("Type a sentence: ").strip()
    sentence_lower = sentence.lower()
    quantity = sentence_lower.count("a")
    first = sentence_lower.find("a") + 1
    last = sentence_lower.rfind("a") + 1
    print(
        "Your sentence has {} letter A's, the first position is {}, and the last is {}".format(
            quantity, first, last
        )
    )

# Exercise 27 - OK
if ex == 27:
    name_parts = input("Type your full name: ").split()
    print("First name: {}".format(name_parts[0]))
    print("Last name: {}".format(name_parts[-1]))  # -1 is always the last element

else:
    print("Invalid exercise!")
