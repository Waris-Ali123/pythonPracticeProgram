print("Program for operator overloading.")
class test:
    def __init__(self,subject1,subject2):
        self.subject1 = subject1
        self.subject2 = subject2

    def show(self):
        
        print("subject1=",self.subject1)
        print("subject2=",self.subject2)

    def __add__(self,other):
        subject1 = self.subject1+other.subject1
        subject2 = self.subject2 + other.subject2
        return test(subject1,subject2)


t1 = test(24,11)
t2 = test(18,17)
t3 = t1+t2
print("Marks of the first test:")
t1.show()
print("Marks of the second test:")
t2.show()
print("Marks after adding:")
t3.show()
    
