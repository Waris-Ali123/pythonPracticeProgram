class circle:
    def  __init__ (self,radius):
        self.radius = radius
    def area (self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

r = int(input("enter the radius of circle :: "))
c1 = circle(r)
a = c1.area()
cir = c1.circumference()
print("area of circle:",a)
print("circumference of circle:",cir)




