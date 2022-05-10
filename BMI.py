#Program for calculating body mass index
print('Program for calculating body mass index')

typ = int( input('Enter 1 for meters&kg and 2 for inches&pound type:') )

if(typ == 1):
    height = float( input('Please enter your height (in meters):') )
    weight = float( input('Please enter your weight(in kg):') )
    
    bmi = weight/( height*height )
    
elif(typ == 2):
    height = float( input('Please enter your height(inches):') )
    weight = float( input('Please enter your weight(pound):') )
    
    bmi = ( weight/(height*height) ) * 703
   
else:
    print('Invalid choice!!!')

print(bmi)

if(bmi <= 18.5):
    print('You are under weight')
elif(18.5 < bmi and bmi <= 24.9):
    print('You have normal weight')
elif(24.9 < bmi and bmi <= 29.9 ):
    print('You are over weight')
else:
    print('You are obesity')
    





'''Output
Program for calculating body mass index
Enter 1 for meters&kg and 2 for inches&pound type:1
Please enter your height:1.76784
Please enter your weight:60
19.1984133472825
>>> 
========== RESTART: C:/Users/asus/OneDrive/Desktop/Python code/BMI.py ==========
Program for calculating body mass index
Enter 1 for meters&kg and 2 for inches&pound type:2
Please enter your height:69.6
Please enter your weight:132.2774
19.196519561699038'''
