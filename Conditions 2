import time
from random import randint

# Exercise table starting from 36

print('\033[1;33m ===Exercise Menu=== \033[m')
print('36 - Bank loan')
print('37 - Number conversion')
print('38 - Number comparator')
print('39 - Age / Military enlistment')
print('40 - Average grade')
print('41 - Swimming category')
print('42 - Triangle classification')
print('43 - BMI')
print('44 - Payment options')
print('45 - Rock Paper Scissors')

exercise = int(input('Enter the exercise number you want to run: '))

if exercise == 36:
    house_price = float(input('\033[4;31m Hello! To approve your house purchase, we need its value: \033[m'))
    time.sleep(2)
    salary = float(input('Ok! Now, we need your \033[1;32m salary:\033[m '))
    time.sleep(1)
    years = int(input('In how many years do you want to pay the house? '))
    monthly_payment = house_price / (years * 12)
    time.sleep(1)

    print(
        'We approve loans that do not exceed 30% of the client salary. '
        'The monthly payment for a house worth ${}, financed over {} years, will be ${:.2f} per month.'
        .format(house_price, years, monthly_payment)
    )

    if salary * 0.3 > monthly_payment:
        print('Loan approved!')
    else:
        print('Loan denied.')

if exercise == 37:
    number = int(input('Enter an \033[1;35m integer \033[m: '))
    choice = int(input('Enter 1 for binary, 2 for octal or 3 for hexadecimal: '))

    if choice == 1:
        print('{} converted to binary is {}'.format(number, bin(number)[2:]))
    if choice == 2:
        print('{} converted to octal is {}'.format(number, oct(number)[2:]))
    if choice == 3:
        print('{} converted to hexadecimal is {}'.format(number, hex(number)[2:]))

if exercise == 38:
    n1 = int(input('Enter the \033[1;31m first number:\033[m '))
    n2 = int(input('Enter the \033[1;32m second number:\033[m '))

    if n1 > n2:
        print('The \033[1;31m first value\033[m is greater.')
    elif n1 < n2:
        print('The \033[1;32m second value\033[m is greater.')
    else:
        print('Both values are equal.')

if exercise == 39:
    age = int(input('How old are you? '))

    if age < 18:
        print('You will enlist in {} years.'.format(18 - age))
    elif age == 18:
        print('It is time to enlist!')
    else:
        print('You should have enlisted {} years ago.'.format(age - 18))

if exercise == 40:
    grade1 = float(input('What grade did you get on the first test? '))
    grade2 = float(input('What grade did you get on the second test? '))
    average = (grade1 + grade2) / 2

    if average < 5.0:
        print('Failed.')
    elif 5.0 <= average < 7.0:   #Here we are considering Brazillian grade system, which is from 0 to 10, being 0 the worst and 10 the best.
        print('Recovery.')
    else:
        print('Approved.')

if exercise == 41:
    birth_year = int(input('In which year were you born? '))
    current_year = 2026
    age = current_year - birth_year

    if age < 9:
        print('Your category is Mirim.')
    elif 9 <= age <= 14:
        print('Your category is Infantil.')
    elif 14 <= age <= 19:
        print('Your category is Junior.')
    elif 20 <= age < 21:
        print('Your category is Senior.')
    else:
        print('Your category is Master.')

if exercise == 42:
    side1 = int(input('Enter the length of the first side: '))
    side2 = int(input('Enter the length of the second side: '))
    side3 = int(input('Enter the length of the third side: '))

    sides = sorted([side1, side2, side3])

    if sides[0] + sides[1] <= sides[2]:
        print('It will not form a triangle.')
    else:
        if sides[0] == sides[1] == sides[2]:
            print('It will form an equilateral triangle.')
        elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            print('It will form an isosceles triangle.')
        else:
            print('It will form a scalene triangle.')

if exercise == 43:
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height in meters: '))
    bmi = weight / (height ** 2)

    print('BMI:', bmi)

    if bmi < 18.5:
        print('You are underweight.')
    elif 18.5 <= bmi < 25:
        print('You are at an ideal weight.')
    elif 25 <= bmi < 30:
        print('You are overweight.')
    elif 30 <= bmi < 40:
        print('You have obesity.')
    else:
        print('You have morbid obesity.')

if exercise == 44:
    price = float(input('What is the product price? '))
    time.sleep(1)

    option = input(
        f'Ok, ${price}.\n'
        'Enter 1 to pay cash with 10% discount,\n'
        '2 to pay by card with 5% discount,\n'
        '3 to split into up to 2 installments with no interest,\n'
        'or 4 to split into 3 or more installments with 20% interest: '
    )

    if option == '1':
        print('Final price: {:.2f}'.format(price * 0.9))
    elif option == '2':
        print('Final price: {:.2f}'.format(price * 0.95))
    elif option == '3':
        print('Final price: {:.2f}'.format(price))
    elif option == '4':
        print('Final price: {:.2f}'.format(price * 1.2))
    else:
        print('Invalid option.')

if exercise == 45:
    computer = randint(1, 3)
    player = int(input('Enter 1 for paper, 2 for rock or 3 for scissors: '))

    if computer == player:
        print('Draw!')
    elif (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
        print('Computer wins!')
    else:
        print('Player wins!')
