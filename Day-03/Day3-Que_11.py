# find the max elem in the given list.
'''
list=list(map(int,input().split()))
max=list[0]
for i in range(0,len(list)):
    if(list[i]>max):
      max=list[i]
print(max)
'''
#min elem in the list
list=list(map(int,input().split()))
min=list[0]
for i in range(0,len(list)):
    if(list[i]<min):
      min=list[i]
print(min) 
