#Program for prime number using for and else statement

n = int(input("Please enter a number:"))
if(n<2):
    print("Invalid")
else:
    for i in range(2,n//2+1,1):
        if(n%i==0):
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
    
    
