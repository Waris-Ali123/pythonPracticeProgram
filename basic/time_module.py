#time module
import time as t #Syntax to import time module and alias it as t
print(t.localtime())  #function to access the current date time and day

print('------------------------------------------------------------------------')

time_now = t.localtime()       #returning the localtime function and printing only the values that are required
print('Transaction completed at',str(time_now.tm_hour)+'h'+str(time_now.tm_min)+'m')

print('------------------------------------------------------------------------')

print(t.time())    # time() function returns the seconds from the 1st Jan 1970 and called as appuk 
t.sleep(2)        # this is the sleep times that stops the execution for n no. of seconds and is very useful for making timer

print(t.time())    #it is contineously increasing 
t.sleep(1)
print(t.time())

print('------------------------------------------------------------------------')

time_now = t.time()   #storing the time() function value
delivery_time = time_now + (86400 * 7)     #calculating the seconds of seven days and then adding it to the time_now to get the seconds when the thing will be delivered
print('Delivery time:')    
print(t.localtime(delivery_time))      #using that seconds we can calculate the day and the date as well
