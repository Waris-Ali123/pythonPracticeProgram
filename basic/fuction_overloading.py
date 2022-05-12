print("Program for overridingo")

class A:
    def random(self):
        print("I'm in class A")

class B(A):
    def random(self):
        print("I'm in class B")

item1 = B()
item1.random()
