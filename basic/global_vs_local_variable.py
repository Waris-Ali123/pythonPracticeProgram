count = 1  #Global variable i.e  it may execute in the program
def plus():
    global count
    count += 1
def minus():
    global count
    count -=1

print('count = ',count)
plus()
plus()
print('count = ',count)
minus()
minus()
print('count=',count)
