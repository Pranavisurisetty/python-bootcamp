# armstrong or not

n=int(input())
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit*digit*digit
    temp=temp//10
if sum==n:
    print("it is an Armstrong number")
else:
    print("it is not a Armstrong number")


