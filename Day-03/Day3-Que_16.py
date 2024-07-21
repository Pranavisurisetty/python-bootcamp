# sum of square of digits
'''
n=123
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem*rem
    n=n//10
print(sum) 
'''
# sum of even numbers
# n=1234
# sum=0
# while(n>0):
#     rem=n%10
#     if(rem%2==0):
#         sum=sum+rem
#     n=n//10
# print(sum) 

'''
# reverse of a num(metho-1)
n=1234
sum=0
while(n>0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
print(sum) 
'''
# reverse of a num(method-2)
n=1234
rev=""
while(n>0):
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))