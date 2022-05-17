class student:
    institution = "iips"

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        print("--------------------------------------------------------------------------------")
        print("Marks in python:",self.a)
        print("Marks in python lab:",self.b)
        print("--------------------------------------------------------------------------------")

    @classmethod
    def info(self):
        print("Class belongs to",self.institution)

    @staticmethod
    def about():
        print("This class holds the data of marks obtained by students")



s1 = student(14,19)
s2 = student(15,13)

s1.show()
s2.show()

student.info()
s1.about()
student.about()
