#Program for combination using user defined module

print('Program to calculate combination using user defined module')
import fact_function as f

n = int(input('Please enter the total items:'))
r = int(input('Enter the no. of item to be arranged:'))

fn = f.fact(n)
fnr = f.fact(n-r)
fr = f.fact(r)

p = fn/(fnr * fr)

print('The combination be:',p)
