# print the no.of consonants in the give string

string=input()
# check=['a','e','i','o','u']
lst='bcdfghjklmnpqrstuwxyz'
count=0
for i in string:
    if((i in lst)):
        count+=1
print(count)


