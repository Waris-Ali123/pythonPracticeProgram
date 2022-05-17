n = int(input("Please enter a number to write a table"))

for i in range(1,11):
    print(n,"*",i,"=",n*i)


print("-------------------------------------------------")

m = n*10

for i in range(n,m+1,n):
    print(n,"*",i//n,"=",i),

print("--------------------------------------------------")

count = 1
for i in range(n,m+1,n):
    print("{} * {} = {}".format(n,count,i))
    count = count+1

print("--------------------------------------------------")

p = 1
for i in range(n,m+1,n):
    print(n,"*",p,"=",i)
    p=p+1


   

    
