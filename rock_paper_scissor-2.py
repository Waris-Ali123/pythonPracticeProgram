#program for game(rock,paper,scissor) where User-01 is person and U2 is computer
import random
ch = 9

while(ch==9):
    
    print("1 for Rock")
    print("2 for Paper")
    print("3 for Scissor")

    U1 = int(input("Please enter your choice number,User-01: "))
    U2 = random.randint(1,3)

    if(U1 == 1 and U2 == 3 or U1 == 2 and U2 == 1 or U1 == 3 and U2 == 2):
        print("You Wins")

    elif(U2 == 1 and U1 == 3 or U2 == 2 and U1 == 1 or U2 == 3 and U1 == 2):
        print("Computer Wins")
        print("You lose")
    elif(U1 == U2):
        print("_______________Draw____________")
    else:
        print("Please enter a correct choice:")

    ch = int(input("Type 9 for continue and 0 for End: "))
else:
    print("Thankyou")





