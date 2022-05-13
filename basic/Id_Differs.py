#program for showing that the id differs for the folowing strings.
s2 = 'tohid'
s3 = 'Tohid'

print(id(s2))
print(id(s3))

print('---------------------------------------------------------------------')

'''But the id will not differ in the following case:'''
a = 5
b = 5

print(id(a))
print(id(b))
