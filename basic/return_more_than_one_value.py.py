
#function to take input
def user_input():
    a = int(input("Enter a value:"))
    b = int(input('Enter another value:'))
    c = int(input('Enter a vlau:'))
    return (a,b,c)

#function to add
def add(a,b,c):
    return a+b+c

a,b,c = user_input()
print(a,'+',b,'+',c,'=',add(a,b,c))
    
