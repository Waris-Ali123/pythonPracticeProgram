
def even(n):
    return n%2==0

list1 = [5,63,2,56,32,45,1,98,1230]

list_even = list(filter(even,list1))
print(list1)
print(list_even)
