#Here i starting asking tips to ChatGPT on how to write cleaner codes
print('-=-'*15)
print('\033[4;32mExercises Menu\033[m')
print('-=-'*15)

print('[78] Beginner list')
print('[ 79 ] List with only single numbers')
print('[ 80 ] Sorting without sort')
print('[ 81 ] Extracting data of a list')
print('[ 82 ] Inserting values in other lists')
print('[ 83 ] Validating a mathematical expression')

ex = int(input('Type in the number of the exercise you want to execute: '))

if ex == 78:
    numbers = []

    for c in range(5):
        n = int(input(f'Insert a value ({c + 1} of 5): '))
        numbers.append(n)

        if c == 0:
            smallest = largest = n
        else:
            if n > largest:
                largest = n
            if n < smallest:
                smallest = n

    print(f'You inserted the numbers {numbers}.') # print all the numbers
    print(f'The smallest number is {smallest}, in the position ', end='')
    for i, v in enumerate(numbers):
        if v == smallest:
            print(f'{i}...', end='')
    print(f'\nThe largest number was {largest}, in the position ', end='')
    for i, v in enumerate(numbers):
        if v == largest:
            print(f'{i}...', end='')
    print()

elif ex == 79:
    numbers = list()
    trashcan = list()
    n_amount = 1
    while True:
        n = int(input(f'Type in an integer number ({n_amount}): '))
        if n not in numbers:
            numbers.append(n)
        else:
            trashcan.append(n)
        c = str(input('Type Y/N to continue or not: ')).upper()[0]
        while c not in 'YN':
            c = str(input('Type Y/N to continue or not: ')).upper()[0]
        if c == 'N':
            break
    print(f'The numbers inserted were {sorted(numbers)}')
    print(f'Duplicates ignored: {trashcan}')

elif ex == 80:
    numbers = list()
    n_amount = 1
    largest = 0
    smallest = 0
    for n in range(0, 5):
        number = int(input(f'Type in an integer number {n_amount}/5: '))
        while number < 0:
            number = int(input(f'Type in a positive integer number {n_amount}/5: '))
        n_amount += 1
        if n == 0:
            numbers.append(number)
            smallest = number
            largest = number
            print('This is the first value received. Inserted on the list.')
        else:
            inserted = False

            for pos in range(len(numbers)):
                if number < numbers[pos]:
                    numbers.insert(pos, number)
                    print(f'Inserted the number {number} in position {pos}')
                    inserted = True
                    break
            if not inserted:
                numbers.append(number)
                print(f'Inserted the number {number} in the end of the list.')

    print(f'The numbers inserted were {numbers}')

elif ex == 81:
    numbers = list()
    while True: #while the user wishes to continue
        number = int(input(f'Type in an integer number: '))
        while number < 0:
            number = int(input(f'Type in a positive integer number: '))
        cont = str(input('Type Y/N to continue or not: ')).upper()[0]
        while cont not in 'YN':
            cont = str(input('Type Y/N to continue or not: ')).upper()[0]
        numbers.append(number)
        if cont == 'N':
            break

    print(f'You inserted a total of {len(numbers)} numbers.')
    print(f'The descending order is: {sorted(numbers, reverse=True)}')
    if 5 in numbers:
        print('The number 5 is in the list.')
    else:
        print('The number 5 aint in the list.')

elif ex == 82:
    numbers = list()
    while True: #until the user type not, itll run the loop
        number = int(input(f'Type in an positive integer number: '))
        while number < 0:
            number = int(input(f'Type in a positive integer number: '))
        numbers.append(number)
        cont = str(input('Type Y/N to continue or not: ')).upper()[0] #validate if the user wants to continue
        while cont not in 'YN': #checks if the user didnt type anything by mistake
            cont = str(input('Type Y/N to continue or not: ')).upper()[0]
        if cont == 'N':
            break
    even_numbers = list()
    odd_numbers = list()
    for num in numbers: # dividing the main list into odd/even lists
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print(f'The numbers typed were {numbers}, '
          f'The even numbers typed were {even_numbers}, '
          f'The odd numbers typed were {odd_numbers}.')

elif ex == 83:
    pile = []
    expression = str(input('Type in an expression: '))
    for symbol in expression:
        if symbol == '(':
            pie.append('(')
        elif symbol == ')':
            if len(pile) > 0:
                pile.pop()
            else:
                pile.append(')')
                break
    if len(pile) == 0:
        print('The expression is valid')
    else:
        print('The expression is invalid')
