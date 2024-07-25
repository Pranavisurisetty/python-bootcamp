# creating a class
#something declared outside the class is called fn. 
# if it is declared inside the class it is know as method
class Myclass:
    def add(a,b): 
        return a+b

#creating an object 
#1.we have to create an instance 
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.add(12,3))