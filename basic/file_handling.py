#File handling
f = open("myfirstfile.txt",'w')
x = "welcome to my first file"
f.write(x)
y = "This file is only for practice"
f.write('\n')
f.write(y)
f.close()

f = open('myfirstfile.txt','r')
z = f.read()
print(z)
f.close()
