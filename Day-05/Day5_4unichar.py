#print the unique characters in a string
string=input()
count=0
ans=""
inp=string.lower()
for i in string:
    if(i in inp):
        if(i not in ans):
          ans+=i
print(ans) #helo wrd