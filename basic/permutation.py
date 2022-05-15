#Program for permutation:

n = int(input("Please enter the items:"))
r = int(input("Enter the number of item to be arranged:"))

#Calculate n factorial
fact_n = 1
for i in range(1,n+1):
    fact_n = fact_n * i


#Calculate n-r factorial
x = n-r
fact_x = 1 

for i in range(1,x+1):
    fact_x = fact_x * i

p = fact_n/fact_x

print("permutation=",p)


