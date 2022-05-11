#program for even odd for floating point numbers

a = input("Please enter a number: ")
a = float(a)

if(a<0):
    print('only positive values are allowed')
else:
    if(a==0):
        print("It is neither even nor odd")
    elif(a%2==0):
        print("Even")
    else:
        print("Odd")






f
