#Program for area and perimeter of circle
print('Program to find area and perimeter of circle.')
#function for area
def area(r):
    a = 3.14*r*r
    print('The area of circle be:',a)

#function for perimeter
def peri(r):
    p = 2 *3.14* r
    print('The perimeter of circle be:',p)

#main block
r = float(input('Please enter radius of circle:'))
area(r)
peri(r)
print('Thankyou')