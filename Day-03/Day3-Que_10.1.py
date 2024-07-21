# print the elem in particular index.(cyclic)
list=list(map(int,input().split()))
n=int(input())
for i in range(0,len(list)):
    rem=n%len(list)
print(rem)
print(list[i])
    