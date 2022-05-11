#Program for checking whether the data entered is correct or not

data_valid = False
while data_valid==False:
    grade1 =  input('Please type the first grade:') 

    try:
        grade1 = float(grade1)
    except:
        print('Type a number only')
        continue
    
    if(grade1<0 or grade1 >10):
        print("The grade can't be less than zero or greater than ten")
        continue
    else:
        data_valid = True

print('You print the correct grade..')


data_valid = False

while data_valid==False:
    grade2 =  input('Please enter the second grade:')
    
    try:
        grade2 = float(grade2)
    except:
        print('Type a number only')
        continue
    
    if(grade2<0 or grade2 >10):
        print("The grade can't be less than zero or greater than ten")
        continue
    else:
        data_valid = True

print('You print the correct grade..')


