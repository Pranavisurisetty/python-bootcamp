# replace the elem in the array with avg of max and min elem.
list=list(map(int,input().split()))
max=list[0]
min=list[0]
for i in range(0,len(list)):
    if(list[i]<min):
      min=list[i]      
    if(list[i]>max):
       max=list[i]
print(min)
print(max)
avg=(max+min)//2
print(avg)
for i in range(len(list)):
     list[i]=avg
print(list)


