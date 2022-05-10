print('Program to find the average of numbers using the function with arbitarary argument')



class student:
    
    def avg(self,* value):
        x = 0
        for i in value:
            x += i

        return x/len(value)


#main function
s1 = student()
n = s1.avg(1,2,3)
print('average=' , n)




