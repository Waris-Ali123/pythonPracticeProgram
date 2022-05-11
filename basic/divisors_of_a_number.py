#Program for finding divisors of a number

n = int(input("Please enter a number to find its divisors:"))
t =0

for i in range(2,n):
    if(n%i==0):
        print(i)
        t = 1
else:
    if(t == 0):
        print("It is a prime number")
    else:
        print("Thankyou")

