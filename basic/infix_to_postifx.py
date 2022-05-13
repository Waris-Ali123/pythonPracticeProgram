print('It is a program for converting infix to postfix')

def create(l):
    res=[]
    i=0
    while(i<len(l)):
        if(l[i].isdigit()):
            if(i==len(l)-1):
                res.append(l[i])
                i+=1
            elif(i!=len(l)-1):
                if(l[i+1].isdigit()):
                    res.append(l[i]+l[i+1])
                    i+=2
                else:
                    res.append(l[i])
                    i+=1
        else:
            res.append(l[i])
            i+=1
    return res

def convert(infix):
    postfix = []   #To store the digits
    stk = []          #To store the operators
    prior = {'+':1,'-':1,'*':2,'/':2,'^':3}        #precedence
    for i in infix:                          #loop for each item in infix expression
        if(i.isdigit()):           #To check whether it is digit  then append in postfix 
            postfix.append(i)
        elif(i == '('):      #IF it is opening parenthesis
            stk.append(i)
        elif(i == ')'):      #if it is closing parenthesis then pop the stack items until you get an opening parenthesis
            while(stk[-1] != '('):
                postfix.append(stk.pop())
            stk.pop() #to pop the opening parenthesis
        else:                       #if it is an operator
            while( stk and stk[-1]!='(' and prior[i]<=prior[ stk[-1] ] ):    #condition to check stack is not null and it is not an opening parenthesis and the i's priority is not less than stack's top priority
                postfix.append( stk.pop() )
            stk.append(i)
    while( stk != [] ):
                postfix.append( stk.pop() )

    return postfix


infix = input('Please enter an expression:')
infix = list(infix)
infix = create(infix)
postfix = convert(infix)
print(postfix)
