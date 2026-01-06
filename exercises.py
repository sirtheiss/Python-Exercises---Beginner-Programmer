import math
from math import ceil
import random
import os

# COLORS
colors = {
    'clear': '\033[m',
    'red': '\033[0;31m',
    'green': '\033[0:32m'
}

print("=== Exercises Menu ===")
print("16 - Integer part of a number")
print("17 - Calculate the hypotenuse of a right triangle")
print("18 - Sine, Cosine and Tangent")
print("19 - Teacher chooses a random student to read a book")
print("191 - Teacher chooses a random student to read a book V2.0")
print("20 - Teacher sorts presentation order")
print("201 - Teacher sorts presentation order V2.0")
print("21 - Opening an MP3 file")
print("211 - Opening an MP3 file V2.0")
print("991 - Exercises made with ChatGPT")
print("22 - Uppercase, lowercase")

ex = int(input("Type the number of the exercise you want to execute: "))

# Exercise 16 - Working!
if ex == 16:
    number = float(input("Type a real number: "))
    print(
        "The number {}{}{} has the integer part {}".format(
            '\033[1;31;40m',
            number,
            '\033[m',
            math.trunc(number)
        )
    )

# Exercise 17 - Working!
elif ex == 17:
    leg1 = float(input("Type the value of the first leg: "))
    leg2 = float(input("Type the value of the second leg: "))
    hypotenuse = math.hypot(leg1, leg2)
    print("The hypotenuse of the triangle is {:.2f}".format(hypotenuse))

# Exercise 18 - Working!
elif ex == 18:
    angle = float(input("Type the angle value: "))
    radians = math.radians(angle)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)
    print(
        "The sine is {:.2f}, the cosine is {:.2f}, and the tangent is {:.2f}".format(
            sine, cosine, tangent
        )
    )

# Exercise 19 - Working!
elif ex == 19:
    student = random.randint(1, 4)
    if student == 1:
        print("João, read page 13")
    if student == 2:
        print("Maria, read page 14")
    if student == 3:
        print("José, read page 15")
    if student == 4:
        print("Rebeca, read page 16")
    else:
        pass

# Exercise 19.1 - Working!
elif ex == 191:
    name1 = input("Type the name of the first student: ")
    name2 = input("Type the name of the second student: ")
    name3 = input("Type the name of the third student: ")
    name4 = input("Type the name of the fourth student: ")
    students = [name1, name2, name3, name4]
    chosen = random.choice(students)
    print(chosen)

# Exercise 20 - Working!
elif ex == 20:
    students = ["João", "Maria", "José", "Rebeca"]
    random.shuffle(students)
    print("Random order:", students)

# Exercise 201 - Working!
elif ex == 201:
    name1 = input("Type the name of the first student: ")
    name2 = input("Type the name of the second student: ")
    name3 = input("Type the name of the third student: ")
    name4 = input("Type the name of the fourth student: ")
    students = [name1, name2, name3, name4]
    random.shuffle(students)
    print(students)

# Exercise 21 - Working!
elif ex == 21:
    file_path = "C:/Users/user/OneDrive/Desktop/mp3/music.mp3"
    os.startfile(file_path)

# Exercise 211 - Working!
elif ex == 211:
    pygame.init()
    pygame.mixer.music.load("ex021.mp3")
    pygame.mixer.music.play()

# Exercise CG1 - Working!
elif ex == 991:
    n = int(input("Enter a value: "))
    print(
        "The number {} has square root {}, factorial {}, and its value rounded up is {}".format(
            n,
            math.sqrt(n),
            math.factorial(n),
            ceil(n)
        )
    )

else:
    print("Invalid exercise!")
