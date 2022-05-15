print("Program for method overloading")

class student:
    def avg(self,a=None,b=None,c=None):
        average = 0
        if(a!=None and b!= None and c!=None):
            average = (a+b+c)/3
        elif(a!=None and b!= None and c== None):
            average = (a+b)/2
        elif(a!=None and b==None and c==None):
            average = a
        else:
            average = "No Values Provided"

        return average


s1 = student()
print("The average be",s1.avg(1,2,3) )
print("The average be",s1.avg(1,2) )
print("The average be",s1.avg(1) )
print("The average be:",s1.avg() )
