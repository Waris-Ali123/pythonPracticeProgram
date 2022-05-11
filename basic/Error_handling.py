#Program for error handling.
number = input('Please enter a number:')

try:
    number = float(number)
    print('The user entered the number not string.')
except:
    print('Invalid character..I want a number only')
