#USING CONDITIONALS
import random
import time

# Exercises table starting from 28

print("=== Exercises Menu ===")
print("28 - Guess the number")
print("29 - Car speed and fine")
print("30 - Even or odd?")
print("31 - Travel price")
print("32 - Leap year")
print("33 - Ascending order")
print("331 - Ascending order V2.0")
print("34 - Salary increase")
print("35 - Triangle")

ex = input("Type the number of the exercise you want to execute: ")

# Exercise 28
if ex == "28":
    computer_number = random.randint(0, 5)
    player_number = input("The computer chose a number between 0 and 5... Try to guess: ")
    if computer_number == player_number:
        print("You got it right!")
    else:
        print("You got it wrong!")
    print(computer_number)

# Exercise 29
if ex == "29":
    speed = int(input("How fast are you going (in km/h)?: "))
    if speed > 80:
        print("\033[31mYou exceeded the speed limit!\033[m")
        fine = (speed - 80) * 7
        print("You must pay R${} as a fine".format(fine))
    else:
        print("You are within the speed limit!")

# Exercise 30
if ex == "30":
    number = int(input("Type any integer number: "))
    if number % 2 == 0:
        print("{} is even".format(number))
    else:
        print("{} is odd".format(number))

# Exercise 31
if ex == "31":
    distance = float(input("How many kilometers is the trip you are going to take?: "))
    print("Analyzing prices...")
    time.sleep(0.5)
    if distance <= 200:
        print(
            "Your trip of {} km will cost R${:.2f} with a price of R$0.50 per kilometer.".format(
                distance, distance * 0.5
            )
        )
    else:
        print(
            "Your trip of {} km will cost R${:.2f} with a price of R$0.45 per kilometer.".format(
                distance, distance * 0.45
            )
        )

# Exercise 32
if ex == "32":
    year = int(input("Leap year calculator, enter the year you want to check: "))
    if year % 4 == 0:
        print("The year {} is a leap year".format(year))
    else:
        print("The year {} is not a leap year".format(year))

# Exercise 33
if ex == "33":
    n1 = int(input("Type the first value: "))
    n2 = int(input("Type the second value: "))
    n3 = int(input("Type the third value: "))
    if n1 > n2 > n3:
        print("The highest is {}, followed by {} and {}".format(n1, n2, n3))
    elif n2 > n3 > n1:
        print("The highest is {}, followed by {} and {}".format(n2, n3, n1))
    elif n3 > n1 > n2:
        print("The highest is {}, followed by {} and {}".format(n3, n1, n2))
    elif n1 > n3 > n2:
        print("The highest is {}, followed by {} and {}".format(n1, n3, n2))
    elif n2 > n1 > n3:
        print("The highest is {}, followed by {} and {}".format(n2, n1, n3))
    elif n3 > n2 > n1:
        print("The highest is {}, followed by {} and {}".format(n3, n2, n1))
    else:
        pass

# Exercise 331
if ex == "331":
    n1 = int(input("Type the first value: "))
    n2 = int(input("Type the second value: "))
    n3 = int(input("Type the third value: "))

    numbers = [n1, n2, n3]
    sorted_numbers = sorted(numbers, reverse=True)

    print("The highest is {}, followed by {} and {}".format(*sorted_numbers))

# Exercise 34
if ex == "34":
    salary = float(input("Type your salary: "))
    if salary <= 1250.0:
        print(
            "You will receive a 15% increase, your salary will be R${}".format(
                salary + salary / 10 + salary / 20
            )
        )
    else:
        print(
            "You will receive a 10% increase, your salary will be R${}".format(
                salary + salary / 10
            )
        )

# Exercise 35
if ex == "35":
    line1 = int(input("Type the value of the first line: "))
    line2 = int(input("Type the value of the second line: "))
    line3 = int(input("Type the value of the third line: "))
    lines = [line1, line2, line3]
    sorted_lines = sorted(lines)
    if sorted_lines[0] + sorted_lines[1] > sorted_lines[2]:
        print("It will form a triangle!")
    else:
        print("It will not form a triangle.")

else:
    print("Invalid exercise!")
