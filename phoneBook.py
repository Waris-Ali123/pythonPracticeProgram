#Phonebook

class Contact:
    def __init__ (self,f_name,l_name,email,catogary,address,number1,number2,):                                           #address,contact1,contact2,email,first_name,last name,catogary
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.catogary = catogary
        self.address = address
        self.number1 = number1
        self.number2 = number2
        
    def putdata(self):                                                    #function to write the data in our file
        f = open("phonebook.txt","a")

        f.write(self.f_name)
        f.write(',')
        f.write(self.l_name)
        f.write(',')
        f.write(self.email)
        f.write(',')
        f.write(self.catogary)
        f.write(',')
        f.write(self.address)
        f.write(',')
        f.write(self.number1)
        f.write(',')
        f.write(self.number2)
        f.write('\n')
        f.close()

#END OF CLASS
        
def getdata():                                                                                  #function to fetch the data from file
        f = open("phonebook.txt","r")
        temp = f.read()
        f.close()
        return temp

def see_in_table():
    l = getdata().split(',')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(" firstName \t | lastName \t | Email \t\t| Catogary  \t| Address \t\t | Contact-01 \t | Contact-02  \t |")
    for i in range(0,len(l)-1,7):
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(l[i] ,"\t\t |",l[i+1],"\t\t |",l[i+2],"\t\t |",l[i+3],"\t\t |",l[i+4],"\t\t |",l[i+5],"\t\t |",l[i+6],"\t\t |")
            
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
    
    
#MAIN FUNCTION()
limit = int( input('How many enteries you wanna to insert:') )   
for i in range(limit):
    f_name= input("Please enter your first name:")
    l_name = input("Please enter your last name:")
    email = input("Please enter your email:")
    catogary = input("Please enter the catogary:")
    address = input("Please enter the address:")
    number1 = input("Please enter the first number:")
    number2 = input("Please enter the second number:")
  


    
    c = Contact(f_name,l_name,email,catogary,address,number1,number2)
    c(i+1).putdata()                              
    
see_in_table()










''' list1 = []
    list1 = getdata()
print("Name\t","Number\n",list1)'''





'''  data_valid = False                                          #fetching the correct number from user
    while data_valid == False:
        number = input("Please enter a number:")
        try:
            number = int(number)
            data_valid =True
        except:
            print("Type a number only")
            continue


    number = str(number)'''
