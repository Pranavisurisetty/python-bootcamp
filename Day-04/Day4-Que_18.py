# prime or not using sq.root method
a=int(input("Enter a num:"))
count=0
r=a**0.5
if(a==1):
    print("invalid")
elif(a==2):
    print("is a prime num")
for i in range(2,int(r+1)):
    if(a%i==0):
        count=1
        break
if count==0:
    print("it is a prime num")
else:
    print("not a prime num")

