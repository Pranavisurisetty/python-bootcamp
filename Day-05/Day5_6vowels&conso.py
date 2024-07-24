# write a program to print vowels followed by consonats
string="hello world"
vowels=['a','e','i','o','u']
conso="bcdfghjklmnpqrstuwxyz"
ans=""
inp=string.lower()
count=0
for i in inp:
    if((i in vowels)):
        ans+=i
for i in inp:
    if(i in conso):
        ans+=i
print(ans) #eoohllwrld