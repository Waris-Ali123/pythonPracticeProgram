 from functools import reduce

list1 = [5,63,2,56,32,45,1,98,1230]
list_even = list(filter(lambda x : x%2==0 ,list1) )     #it is not used to alter values only to take the values as input

print(list1)
print("even =",list_even)

list_double = list( map(lambda x : x*2,list_even)  )      #map is used to alter the values of the iterable
print("The double of even list:",list_double)

sum1 = reduce(lambda x,y: x+y ,list_even)          #reduce is used to apply the aggragate functiosns eg.sum ,avg
print("The sum of the even list be:",sum1)

