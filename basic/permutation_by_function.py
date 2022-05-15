#Program for finding the permutation using function
#function for factorial
def fact(n):
    fact_n = 1
    for i in range(1,n+1):
        fact_n *= i
    print("Factorial of", n , "=" , fact_n)
    return(fact_n)
    

n = int(input('Please enter the total items:'))
r = int(input('Enter the no. of item to be arranged:'))

x = n-r

fn = fact(n)
fx = fact(x)

p = fn/fx

print('The permutation be:',p)

