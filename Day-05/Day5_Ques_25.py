#print all capital letters in a give string

str="HELLO1234world"
sum=""
for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        sum+=i
print(sum)