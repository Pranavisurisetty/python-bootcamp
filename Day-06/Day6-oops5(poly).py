# method over-loading(compile time)
class cal:
    def add(self,*args): #self will take care of the dynamic inputs and memory
        return sum(args)
    
    
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(2,3,4,5,))