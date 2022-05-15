#Program for evaluating the permutation  using imported factorial program

print('Program to calculate permutation using user defined module')
import fact_function as f

n = int(input('Please enter the total items:'))
r = int(input('Enter the no. of item to be arranged:'))

fn = f.fact(n)
x = n-r
fx = f.fact(x)

p = fn/fx

print('The permutation be:',p)
