a, b, c = input("Please enter three number: ").split()

#print(int(a)+2)
a = int(a)
b = int(b)
c = int(c)
#b = int(input("Enter a second number: "))
#c = int(input("Enter one more number: "))

if(a==b and a==c):
    print("All numbers are same")
 
elif(a>b):
    if(a>c):
        print(a," is a greater than", b," and ", c)
    else:
        print(c," is a greater than", a, " and " , b)
else:
    if(b>c):
        print(b," is a greater than",a,"and",c)
    else:
        print(c,"is a greater than",a, "and",b)
        
#not working good in case of   5    5     1
.
