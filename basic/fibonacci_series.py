o#Program for making fibanacci series

n =  int(input("Please enter the length of fibonacci series:"))
n1 = 0
n2 = 1
print("The series is as follows:")
print(n1)
print(n2)

for i in range(0,n-2):
    sum = n1 + n2
    n1 = n2
    n2 = sum
    print(sum,"\t")
