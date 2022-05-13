#Program for finding LCM
print('Program for finding LCM')

#function to calculate LCM
def calculate_LCM(n1,n2):
   
        if(n1>n2):
            higher = n1
        else:
            higher = n2
            
        temp = higher

        while(True):
            if(higher%n1==0 and higher%n2==0):
                print('The LCM of',n1,'and',n2,'is',higher)
                break
            else:
                higher = higher + temp

  

n1 = int(input('Please enter first number:'))
n2 = int(input('Please enter second number:'))

calculate_LCM(n1,n2)
