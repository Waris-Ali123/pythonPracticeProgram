#Program for concatinating the tuples and answer of question that how the tuples gets concatinated even it is mutable
t1 = ('waris')
t2 = ('ALi')
print(t1)
print(id(t1))
t1 = t1+t2
print(t1)
print(id(t1))
print('--------------------------------------')
#same by using list

l1 = ['waris']
l2 = ['ali']
print(l1)
print(id(l1))
l1 += l2
print(l1)
print(id(l1))

