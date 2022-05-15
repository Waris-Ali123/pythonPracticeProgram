#Prongram to check for prime number

n = int(input("Please enter a number:"))

if(n < 2):
    print('Invalid')

else:
    i = 2
    t = 1
    while(i<(n//2+1)):
        if(n%i==0):
            t = 0
            break
        i+=1
    
    if(t == 1):
         print(n,"is a prime number")
    else:
         print(n,"is not a prime number")
    

        


'''elif(n==2):
    print("2 is a prime number")'''
