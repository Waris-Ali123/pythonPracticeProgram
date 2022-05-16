#program for swapping using arithematic method
print("Please choose the type of values(integer of float):")
ch=input("press i for integer and f for float:")
if(ch=='i' or ch=='I'):
    a=int(input("Please enter the first number:"))
    b=int(input("Please enter the second number:"))
    print("values before swapping are:")
    print("value of a is:",a)
    print("value of b is:",b)
    a = a+b
    b = a-b
    a = a-b
    print("values after swapping are:")
    print("value of a is:",a)
    print("value of b is:",b)
elif(ch=='f' or ch=='F'):
    a=float(input("Please enter the first number:"))
    b=float(input("Please enter the second number:"))
    print("values before swapping are:")
    print("value of a is:",a)
    print("value of b is:",b)
    a = a+b
    b = a-b
    a = a-b
    print("values after swapping are:")
    print("value of a is:",a)
    print("value of b is:",b)
else:
    print("please enter correct choice!!")
