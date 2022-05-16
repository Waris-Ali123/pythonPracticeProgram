#program for string reversal using swapping
s = input("Please enter a string to reverse:")
l=len(s)
print("string before reversing is:",s)

for i in range(l-1,-1,-1):
    print( s[i] )

s = list(s)  #This is used bcz string cant be manipulated but the list can be
for i in range(0,l//2,1):
    t = s[i]
    s[i] = s[l-i-1]
    s[l-i-1] = t

print(''.join(s))    #This is used only to make list look like string

'''To swap again with a new technique'''

for i in range(0,l//2,1):
    s[i],s[l-i-1]=s[l-i-1],s[i]

print(''.join(s)) #This is used only to make list look string
