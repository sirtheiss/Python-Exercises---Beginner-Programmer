from time import sleep
from random import randint
print('=== \033[4;31mExercises Menu \033[m===')

print('[ 66 ] Breaking a simple loop')
print('[ 67 ] Times table')
print('[ 68 ] Odd or even')
print('[ 69 ] Age and sex')
print('[ 70 ] Cashier')
print('[ 71 ] ATM')

ex = int(input('Type in the exercise number you want to execute: '))

if ex == 66:
    number = 0
    count = 0
    sum = 0
    while True:
        number = int(input('Insert a value: '))
        if number == 999:
            break
        count += 1
        sum += number
    print(f"You've typed {count} numbers, and their sum is {sum}")

if ex == 67:
    number = 1
    multi = 1
    answer = ''
    brk = ''
    while True:
        number = int(input('Type in an integer number: '))
        if number <0:
            print("You've typed a negative number, Times Table program finished.")
            sleep(.5)
            break
        count = 1
        while count < 11:
            multi = number * count
            print(end=f'{number} x {count} equals {multi}\n' if count < 11 else '\n')
            count += 1
        sleep(2)
        while True:
            keepgoing = str(input('Do you wish to continue? [Y/N]').upper().strip())
            if keepgoing == 'Y':
                break
            elif keepgoing == 'N':
                print('Goodbye!')
                exit()
            else:
                print('Please type in Y or N')
                option = str(input('Do you wish to continue? [Y/N]').upper().strip())

if ex == 68:
    print('-=' * 30)
    print("LET'S PLAY ODD OR EVEN")
    print('-=' * 30)
    number_player = 0
    number_computer = 0
    odd_or_even = ''
    streak = 0
    while True:
        number_player = int(input('Type in an integer number between 0 and 10: '))
        odd_or_even = str(input('Type in if you wanna be odd [O] or even [E]')).upper().strip()
        number_computer = randint(0, 10)
        if odd_or_even == 'O':
            if (number_player + number_computer) % 2 != 0:
                print("You won!")
                streak += 1
            else:
                print("You lost.")
                break
        elif odd_or_even == 'E':
            if (number_player + number_computer) % 2 == 0:
                print("You won!")
                streak += 1
            else:
                print("You lost.")
                break
        else:
            print('You inserted an invalid option, please try again')
    print(f'GAME OVER, You had a streak of {streak} wins!')

elif ex == 69:
    age = 0
    sex = ''
    man_count = 0
    majority_count = 0
    under_20_females = 0
    while True:
        sex = str(input('Type in the gender of a person: [M/F]').upper().strip())
        if sex not in ('M', 'F'):
            print('Please, type in [ M ] or [ F ]')
            continue
        age = int(input('Type in the age of a person: ').strip())
        if sex == 'M':
            man_count += 1
        if age >= 18:
            majority_count += 1
        if sex == 'F' and age < 20:
            under_20_females += 1
        continuing = str(input('Do you wish to continue? [Y/N]').upper().strip())
        if continuing == 'N':
            break
        elif continuing != 'Y' and continuing != 'N':
            print('Please type in Y or N')
            pass
        else:
            pass
    print(f"You've inserted {man_count} men, "
          f"{majority_count} person(s) above 18 years old and "
          f"{under_20_females} under 20 years old females.")

elif ex == 70:
    print('-=' * 30)
    print(" \033[4;31mWELCOME TO THEISS'S SUPERMARKET!\033[m ")
    print('-=' * 30)
    total_spent = 0
    over_1000_products = 0
    cheapest_name = ''
    total_products = 0
    product_price = 0
    other_products = ''
    product_name = ''
    cheapest_price = 0
    while True:
        product_name = str(input('Type in the name of the product: ')).strip()
        if total_products == 0:
            cheapest_name = product_name
        product_price = float(input('Type in the price of your product: '))
        if cheapest_price == 0:
            cheapest_price = product_price
        if product_price < cheapest_price:
            cheapest_price = product_price
            cheapest_name = product_name
        total_spent += product_price
        total_products += 1
        if product_price > 1000:
            over_1000_products += 1
        other_products = input('Do you have any other products? [Y/N] ').upper().strip()
        while other_products not in ['Y', 'N']:
            print('Please type in Y or N')
            other_products = input('Do you have any other products? [Y/N] ').upper().strip()

        if other_products == 'N':
            print('Goodbye!')
            break

    print(f"In total, you've spent {total_spent} money. "
          f"\nThere was/were {over_1000_products} products that costed more than USD1000.00. "
          f"\nThe cheapest product was {cheapest_name}")

elif ex == 71:
    print('-=' * 30)
    print(f'\033[1;34m           ATM \033[m')
    print('-=' * 30)
    amount = int(input('Insert the amount to withdraw: '))

    bill_50 = bill_20 = bill_10 = bill_1 = 0
    amount_left = amount

    while amount_left > 0:
        if amount_left >= 50:
            bill_50 += 1
            amount_left -= 50
        elif amount_left >= 20:
            bill_20 += 1
            amount_left -= 20
        elif amount_left >= 10:
            bill_10 += 1
            amount_left -= 10
        else:
            bill_1 += 1
            amount_left -= 1

    print(f'Finished withdrawing {amount} dollars.')
    print(f'{bill_50} x $50')
    print(f'{bill_20} x $20')
    print(f'{bill_10} x $10')
    print(f'{bill_1} x $1')












