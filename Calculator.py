#Program to make a calculator

import math

print("Welcome to Waris calculator.")

#function to add
def addition(a,b):
    return a+b

#function for subtraction
def subtraction(a,b):
    return a-b

#function for multiplication
def multiplication(a,b):
    return a*b

#function for division
def division(a,b):
    if(b==0):
        return 'e'
    else:
        return a/b

#function for modulo
def modulo(a,b):
    if(b==0):
        return 'e'
    else:
        return a%b

#function for exponential function
def for_power(a,b):
    return (a**b)

#function for finding square
def for_square(a):
    return (a*a)

#function for finding cube
def cube(a):
    return a*a*a

#function to find the square root
def root(r):
    if(r<0):
        print('negative values has no roots')
    else:
        r = pow(r,0.5)
        return r

#fucntion to check the string whether it is integer or not
def check1(s):
    l = ['-','0','1','2','3','4','5','6','7','8','9']
    for i in s:
        if i not in l:
            print('INVALID CHARACTER!!!')
            exit()



#function to check the string whether it is float or not
def check2(s):
    l = ['-','0','1','2','3','4','5','6','7','8','9','.']
    for i in s:
        if i not in l:
            print('Invalid character!!!')
            exit()


#Main program
ch=9
while(ch == 9):
    d = input('Type i for integer datatype and f for float:')
    
    if(d != 'i' and d!='f'):
        print('Invalid opcode!!!')
        exit()
    
    print('The menu of operations are as follows:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Modulo')
    print('6. Exponential solution')
    print('7. Square of a number')
    print('8.Cube of a number')
    print('9.Square root of a number')

    o = input('Please enter your choice as serial number:')
    check1(o)
    o = int(o)
    
    if(o==1 or o==2 or o==3 or o==4 or o==5 or o==6):
        if(d == 'i'):
            n1 = input('Please enter first value:')
            check1(n1)
            n1 = int(n1)    
            n2 = input('Please enter second value:')
            check1(n2)
            n2 = int(n2)
        elif(d == 'f'):
            n1 = input('Please enter first value:')
            check2(n1)
            n1 = float(n1)
            n2 = input('Please enter second value:')
            check2(n2)
            n2 = float(n2)
        else:
            print('Please type valid character')
            exit()

    elif(o==7 or o==8 or o==9):
        if(d=='i'):
            n1 = input('Please enter a value:')
            check1(n1)
            n1 = int(n1)
        elif(d=='f'):
            n1 = input('Please enter a value:')
            check2(n1)
            n1 = float(n1)
        else:
            print('Type a valid character')
            exit()
            
    else:
        print('Invalid choice')

    

    if(o == 1):
            add = addition(n1,n2)
            print('{} + {} = {}'.format(n1,n2,add))
            
    elif(o==2):
            sub = subtraction(n1,n2)
            print('{} - {} = {}'.format(n1,n2,sub))
            
    elif(o==3):
            mul = multiplication(n1,n2)
            print('{} * {} = {}'.format(n1,n2,mul))
            
    elif(o==4):
            div = division(n1,n2)
            if(div == 'e'):
                print('Division by zero is not allowed')
            else:    
                print('{} / {} = {}'.format(n1,n2,div))
            
    elif(o==5):
            mod = modulo(n1,n2)
            if(mod == 'e'):
                print('Division by zero is not allowed')
            else:
                print('{} % {} = {}'.format(n1,n2,mod))

    elif(o==6):
            p = for_power(n1,n2)
            print('{} ^ {} = {}'.format(n1,n2,p))

    elif(o==7):
            sq = for_square(n1)
            print('{} ^ 2 = {}'.format(n1,sq))

    elif(o==8):
            c = cube(n1)
            print('{} ^ 3 = {}'.format(n1,c))
    elif(o==9):
            r = root(n1)
            print('square root of {} is {}'.format(n1,r))
            
    else:
            print('INVALID CHOICE!!!')

    ch = input('press 0 to end and 9 to continue:')
    check1(ch)
    ch = int(ch)
    if(ch != 0 and ch != 9):
        print('invalid key!!!')
        exit()
    



        

