# polymorphism..
#polymorphism can be achieved by method overloading and overriding in python.
''' method over-riding (run-time)'''
class Animal:
    def speak():
        return "speaking"
class Dog(Animal):
    def speak():
        return "bow"
class puppy(Dog):             # speak() method is over riding 
    def speak():
        return "puppy"
obj1=puppy
print(obj1.speak())

# def run():
#     return "running" 
# def run():
#     return "hello"
# print(run())