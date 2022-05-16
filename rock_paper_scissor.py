#Program for Game(Rock,paper,scissor) where U1 and U2 both are users
c = '9'
while(c == "9"):
    print('1 for Rock')
    print('2 for Scissor')
    print('3 for Paper')

    U1 = int(input("Please enter your choice, User-01!!:"))
    U2 = int(input("Please enter your choice, User-02!!:"))
    

    if(U1 == U2):
        print("...................Match Draw..................")
    
    elif(U1 == 1 and U2 == 2 or U1 == 2 and U2 == 3 or U1 == 3 and U2 == 1):
        print("*******************User_01 Won**************")

    elif(U2==1 and U1 == 2 or U2 == 2 and U1 == 3 or U2 == 3 and U1 == 1):
        print("*******************User-02 Won******************")

    else:
        print("Please fill up the correct value!!!!!!!!!")

    c = input("Type 9 to continue or press enter to exit:")

   

else:
    print("Thankyou")
