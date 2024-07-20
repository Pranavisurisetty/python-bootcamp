#your given with a space separated integer list,
# find no.of even elem and no.of odd elem in a given list..
lst=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(lst)):
    if(lst[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)