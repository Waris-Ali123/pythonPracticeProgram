#program to find the factorial of a number using recursion

#fucntion for factorial
def fact(x):
    if(x==0):
        return 1
    else:
        factorial = x * fact(x-1)
        return factorial


print('Program to find the factorial.')
n = int(input('Please enter a number:'))

print('factorial of {} is {}'.format(n,factorial(n)))
