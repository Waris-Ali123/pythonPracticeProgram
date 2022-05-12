#Program for functions
def say_hello(person1,person2 = 'The director'):
    print('Hello',person1, ", how are you doing",person2,'is waiting for you')

def fahr2celsius(fahr):
    celsuis = ( 5 * (fahr - 32) ) / 9
    return celsuis

say_hello('Jaene')
say_hello('Zishan')
say_hello('Waris')


print('Celsius = ' , round (fahr2celsius(100),2)  )
print('Kelvin = ', round ( fahr2celsius(100) +273.5 , 2 )  )
