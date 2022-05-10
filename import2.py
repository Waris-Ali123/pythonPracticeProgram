#Program for importing a module using alias of module

import math as m
n = int(input("Please enter a number for finding it's square:"))
s = m.pow(n,2)

print('The square of {} is {}'.format(n,s))
