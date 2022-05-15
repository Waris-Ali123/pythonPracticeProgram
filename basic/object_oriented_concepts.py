#Object oriented concepts
class cars:
    def __init__ (self ,b_name,model,typ):
        self.b_name = b_name
        self.model = model
        self.typ = typ


car1 = cars('Maruti','Caiz','Sedan')

print('branch name:',car1.b_name)
print('Model:' , car1.model)
print('Type:',car1.typ)
print(car1)  #will print the address of object
