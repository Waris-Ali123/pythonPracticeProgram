date = input("Please enter Your date of birth in format'01-10-2001':")

m = int(date[3:5])-1

if(m>0 and m<=12):
    list1 = ['January','February','March','April','May','June','July','August','September','October','November','december']
    print('You were born in',list1[m])
else:
    print('Invalid date format')
    
