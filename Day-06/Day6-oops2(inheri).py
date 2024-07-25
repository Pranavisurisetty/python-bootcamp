class Animal:
    def Speak():
        return"Animal is speaking"
class Dog(Animal): #single inherited class
    def Bark():
        return "bow"
class puppy(Dog): #multi level inhe
    def puppy_speak():
        return "Im puppy"
#obj1=Animal
#obj2=Dog
obj3=puppy
print(obj3.Speak())
print(obj3.Bark())
print(obj3.puppy_speak())

    

