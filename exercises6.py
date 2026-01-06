# Started using While
from random import randint
from math import factorial

print('=== \033[4;31mExercise Menu\033[m ===')

print('[ 57 ] Data validation')
print('[ 58 ] Guessing game V2.0')
print('[ 59 ] Creating an options menu')
print('[ 60 ] Factorial')
print('[ 61 ] Arithmetic Progression')
print('[ 62 ] Arithmetic Progression 2')
print('[ 63 ] Fibonacci')
print('[ 64 ] Type 999 to stop')
print('[ 65 ] Average, highest and lowest')

exercise = int(input('\033[2;36mEnter the exercise you want to run:\033[m '))

if exercise == 57:
    gender = ''
    while gender != 'M' and gender != 'F':
        gender = str(input('What is your gender? [M/F]: ').upper())
        if gender == 'M' or gender == 'F':
            break

    if gender == 'F':
        print('You are a woman')
    else:
        print('You are a man')

if exercise == 58:
    computer_number = randint(0, 10)
    player_number = 11
    attempts = 0

    while computer_number != player_number:
        player_number = int(input('Enter a number between 0 and 10: '))
        attempts += 1

    print(f'You got it right! You only needed {attempts} attempts.')

if exercise == 59:
    n1 = int(input('Enter a value: '))
    n2 = int(input('Enter another value: '))
    option = 0

    while option != 5:
        option = int(input(
            'Your options:'
            '\n [ 1 ] add'
            '\n [ 2 ] multiply'
            '\n [ 3 ] greater'
            '\n [ 4 ] enter new numbers'
            '\n [ 5 ] exit'
            '\n Your option: '
        ))

        if option == 1:
            print(f'The sum of {n1} and {n2} is {n1 + n2}')
        elif option == 2:
            print(f'{n1} multiplied by {n2} equals {n1 * n2}')
        elif option == 3:
            if n1 > n2:
                print(f'{n1} is greater than {n2}')
            else:
                print(f'{n2} is greater than {n1}')
        elif option == 4:
            n1 = int(input('Enter a value: '))
            n2 = int(input('Enter another value: '))
        else:
            ...
            continue_program = str(
                input('Invalid command, do you want to try again? [Y/N]')
                .upper()
                .replace(' ', '')
            )

            if continue_program == 'Y':
                print('Ok!')
            else:
                print('Thank you for using my program! Goodbye!')
                break

elif exercise == 60:
    chosen_number = int(input('Enter a value to see its factorial: '))
    result = 1
    n = chosen_number

    while n != 1:
        result *= n
        print(n)
        n -= 1

    print(f'The factorial of {chosen_number} is {result}')

elif exercise == 61:
    first_term = int(input('Enter the first value of an arithmetic progression: '))
    ratio = int(input('Enter the ratio of this arithmetic progression: '))
    counter = 1
    term = first_term

    while counter <= 10:
        tenth_term = term
        print(term, end='->')
        term += ratio
        counter += 1

    print(f'The tenth term of this arithmetic progression is {tenth_term}')

elif exercise == 62:
    first_term = int(input('Enter the first value of an arithmetic progression: '))
    ratio = int(input('Enter the ratio of this arithmetic progression: '))
    target_term = int(input('Enter which term you want to show, type 0 to exit: '))
    counter = 1
    term = first_term

    if target_term <= 0:
        print('Invalid number!')
        exit

    while counter <= target_term:
        nth_term = term
        print(term, end='->')
        term += ratio
        counter += 1

    print(f'The {target_term}th term of this arithmetic progression is {nth_term}')

elif exercise == 63:
    n = int(input('Enter a value: '))
    a = 0
    b = 1
    counter = 0

    while counter < n:
        print(a)
        nth = a
        c = a + b
        a = b
        b = c
        counter += 1

    print(f'The term {n} in the Fibonacci sequence is {nth}')

elif exercise == 64:
    counter = 0
    total = 0
    n = 0

    while n != 999:
        n = int(input('Enter a value (999 to stop): '))
        total += n
        counter += 1

    total -= 999
    counter -= 1

    print(f'{counter} numbers were entered, and their sum is {total}')

elif exercise == 65:
    total = 0
    counter = 0
    numbers = []
    highest = 0
    lowest = 0

    while True:
        n = int(input('Enter a value: '))
        total += n
        counter += 1
        numbers.append(n)

        if counter == 1:
            highest = lowest = n

        if n > highest:
            highest = n
        if n < lowest:
            lowest = n

        continue_input = str(
            input('Do you want to continue?\n [Y]\n [N]')
            .upper()
            .replace(' ', '')
        )

        if continue_input == 'N':
            break

    numbers.sort()
    average = total / counter

    print(
        f'The average of all entered numbers is {average}, '
        f'the highest number was {numbers[-1]}, and the lowest was {numbers[0]}'
    )

    print(
        f'The average of all entered numbers is {average}, '
        f'the highest number was {highest}, and the lowest was {lowest}'
    )
