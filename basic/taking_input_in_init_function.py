print("Program for taking input in init function")

class school:
    def __init__(self):
        self.name = input("Please enter a school name:")
        self.address = input("Please enter the school address:")

    def random(self):
        print("{} is situated at {}".format(self.name,self.address) )
        

s1 = school()
s1.random()
