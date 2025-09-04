# This is mini Python calculator
# Skills - operators, if statements, print

operator = input('Select an operator (-, +, /, *): ')
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))

if operator == '+':
    result = num1 + num2
    print(round(result))
elif operator == '-':
    result = num1 - num2
    print(round(result))
elif operator == '*':
    result = num1 * num2
    print(round(result))
elif operator == '/':
    result = num1 / num2
    print(round(result))
else:
    print(f'{operator} is not valid operator')
