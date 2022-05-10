class cube:
    def  __init__ (self,side):
        self.side = side
    def area (self):
        return 6*self.side*self.side
    def perimeter(self):
        return 12*self.side
    def volume(self):
        return self.side**3
    
s = int(input("enter the radius of circle :: "))
c1 = cube(s)
a = c1.area()
peri = c1.perimeter()
v = c1.volume()
print("area of cube:",a)
print("Perimeter of cube:",peri)
print("Volume of cube:",v)
