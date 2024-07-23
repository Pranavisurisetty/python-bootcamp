#find peek elem

list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
    if(list[i-1]<list[i] and list[i]>list[i+1]):
     peak=list[i]
     print(peak)  
if(list[-1]>list[-2] and list[-1]>count):
   count=len(list)-1
print(list[count])

#swapp two num
'''
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)  
'''
     
