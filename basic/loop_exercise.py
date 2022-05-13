#Create a program that asks the user for 8 names of people and store them in a list. when all the names have been given, pick a random one and print it.
import random
people = []
while len(people)<8:
    name = input ('Please enter  the name of employee: ')
    people.append(name)

'''rand = random.randint(0,len(people)-1)
print(people[rand])'''
print('Picking the random name',random.choice(people))
