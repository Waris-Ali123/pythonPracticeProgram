a = int(input("Please enter  first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a==b and a==c):
    print("All numbers are same")
elif(a>b and a>c):
    print(a," is the greatest")
elif(b>a and b>c):
    print(b," is the greatest")
elif(c>a and c>b):
    print(c, "is the greatest")
elif(a==b):
    if(a>c):
        print("a:",a,"and b:",b, "are equal And c:",c, "is smaller")
    else:
        print("c:",c, "is the greatest And b:", b,"& a:",a,"are equal")
elif(b==c):
    if(a>b):
        print("a:",a,"is the greatest And b:", b,"& c:",c,"are equal")
    else:
        print("a:",a,"is the smaller And b:", b,"& c:",c,"are equal")
elif(a==c):
    if(a>b):
        print("b:",b,"is the smaller And a:", a,"& c:",c,"are equal")
    else:
        print("b:",b,"is the greatest And a:", a,"& c:",c,"are equal")        
