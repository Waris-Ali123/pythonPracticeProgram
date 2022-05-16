str1 = "I am fine"
x=len(str1)
print("Length fo str1 =",x)
print("length of str1 =" + str(x)) #(BCZ it is string concatinating)
print("length fo srt1={}".format(x))

for i in range(x):
    print(str1[i] ,"is at index:", i)

print("-----------------")
for i in range(x):
    print("{} is at index:{}".format(str1[i],i))


for i in str1:    #for printing the indexes only
    print(str1.index(i))

for i in range(x-1,-1,-1): #for printing the reversed string 
    print(str1[i])
