#Program as an exercise of time module
import time as t
times =[]
mistake = 0

print("This is a program that helps you in typing fast. write the word 'Programming' five times")

input('Press enter if you want to play')

while len(times)<5:
    start =  t.time()
    w = input('type the word')
    end = t.time()

    difference = end - start
    times.append(difference)
    if(w.lower()!='programming'):
        mistake += 1

print('You took the time(is seconds) for each turn as follows:',times)
print('And the no. of times you wrote incorrectly:', mistake)
