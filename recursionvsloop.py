#Write a python script to write the execute time for a variable in a file when the variable is used to find factorial using iterative and recursive method
import time as t
f = open('RECURSIONvsLOOP.txt','w')

def fact(x):
    if(x==0):
        return 1
    else:
        return x*fact(x-1)

for num in range(5,996):
    # num = input('Please enter a number to find factorial:')

    f.write(str(num))
    f.write('\t')
    



    #FInding execution time using iteration
    loop_fact = 1
    l_start = t.time()
    for i in range(1,num+1):
        loop_fact = loop_fact * i
    l_end = t.time()
    loop_time = l_end - l_start
    print("Iteration_Time:",loop_time)
    f.write(str(loop_time))
    f.write('\t')


    #Finding time using recursion
    
    r_start = t.time()
    rec_fact = fact(num)
    r_end = t.time()
    recursion_time = r_end - r_start
    print("recTime:",recursion_time)
    f.write(str(recursion_time))
    f.write('\t')


    print('The factorial using iteration:',loop_fact)
    print('The factorial using recursion:',rec_fact)

f.close()
