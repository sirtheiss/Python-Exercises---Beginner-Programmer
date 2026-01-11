# Started using some kind of repeating
import time
import datetime

print('=== \033[4;31mExercise Menu\033[m ===')

print('[ 46 ] Countdown')
print('[ 47 ] Even numbers between 1 and 50')
print('[ 48 ] Sum of all odd multiples of 3')
print('[ 49 ] Multiplication table')
print('[ 50 ] 6 numbers, sum of even ones')
print('[ 51 ] Arithmetic Progression')
print('[ 52 ] Prime number')
print('[ 53 ] Palindrome')
print('[ 54 ] Legal age')
print('[ 55 ] Weight')
print('[ 56 ] Group analysis')

exercise = int(input('\033[2;36mEnter the exercise you want to run:\033[m '))

if exercise == 46:
    for c in range(10, 0, -1):
        print(c)
        time.sleep(1)
    print('Happy New Year!')

if exercise == 47:
    for c in range(0, 51, 2):
        print(c)

if exercise == 48:
    total = 0
    for c in range(0, 501, 3):
        if c % 2 != 0 and c % 3 == 0:
            total += c
    print('Sum:', total)

if exercise == 49:
    print('-=-' * 4)
    number = int(input('Enter a number from 1 to 10 to see its multiplication table: '))
    for c in range(1, 10):
        print(number * (c + 1))

if exercise == 50:
    total = 0
    for c in range(6):
        number = int(input('Enter an integer: '))
        if number % 2 == 0:
            total += number
    print('Sum:', total)

if exercise == 51:
    first_term = int(input('Enter the first term of an AP: '))
    ratio = int(input('Enter the ratio of the AP: '))
    for c in range(first_term, 10, ratio):
        print(c)

if exercise == 52:
    number = int(input('Enter a number to check if it is prime: '))
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for c in range(2, number):
            if number % c == 0:
                is_prime = False
                break

    if is_prime:
        print('{} is prime'.format(number))
    else:
        print('{} is not prime'.format(number))

if exercise == 53:
    sentence = str(input('Enter a sentence: ').lower())
    sentence = sentence.replace(' ', '')
    if sentence == sentence[::-1]:
        print('It is a palindrome!')
    else:
        print('It is not a palindrome.')

if exercise == 54:
    current_year = datetime.date.today().year
    adults = 0
    minors = 0

    for c in range(6):
        birth_year = int(input('Enter your birth year: '))
        age = current_year - birth_year

        if age >= 18:
            adults += 1
            print('Person {}: {} years old - adult'.format(c + 1, age))
        else:
            minors += 1
            print('Person {}: {} years old - minor'.format(c + 1, age))

    print('In this group, {} are adults and {} are minors'.format(adults, minors))

if exercise == 55:
    weights = []
    for c in range(5):
        weight = input('Enter the weight of person {}: '.format(c + 1))
        weights.append(weight)
        weights.sort()

    print(
        'The lightest person weighs {}kg, and the heaviest weighs {}kg'
        .format(weights[0], weights[-1])
    )

if exercise == 56:
    total_age = 0
    women_under_20 = 0
    oldest_man_age = 0
    oldest_man_name = ''

    for p in range(1, 5):
        name = str(input('Enter your name: '))
        age = int(input('Enter your age: '))
        gender = str(input('Enter your gender M/F: '))

        total_age += age

        if gender in 'Mm' and (oldest_man_age == 0 or age > oldest_man_age):
            oldest_man_age = age
            oldest_man_name = name

        if gender in 'Ff' and age < 20:
            women_under_20 += 1

    average_age = total_age / 4

    print('The average age of the group is {}'.format(average_age))
    print('The oldest man is {} and he is {} years old'.format(oldest_man_name, oldest_man_age))
    print('There are {} women under 20 years old'.format(women_under_20))
