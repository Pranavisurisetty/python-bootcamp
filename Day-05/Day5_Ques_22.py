#reverse hello1234world print-->4321
n="hello123world"
a="1234"
b=(int(a))
print(b)
sum=0
while(b>0):
    r=b%10
    sum=sum*10+r 
    b=b//10
print(sum)        