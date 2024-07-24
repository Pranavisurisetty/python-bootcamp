#sum of digits in a num using ascii values. 
str="hello1234world"
sum=0
for i in str:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=str(i)
print(sum) 

