class Area:
    
    def area(l,b):                #area of rectangle
        a = l*b
        return a

    def area(r):                 #area of circle
        a = 3.14*r*r
        return a


#main function

print("1.Area of circle")
print("2.Area of Rectangle")

choice  = int(input("Please type your choice number:") )

if(choice == 1):
    r = int(input("Please enter the radius of circle:") )
    print("The area of circle : ",area(r))

elif(choice == 2):
    l = int(input("Please enter the length of rectangle:") )
    b = int(input("Please enter the breadth of rectangle:") )
    print("The area of rectangle:",area(l,b))
else:
    print("Please enter valid choice!!!!")

    








