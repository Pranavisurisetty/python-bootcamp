#check how many vowels are there in a string
string=input()
check=['a','e','i','o','u']
count=0
for i in string:
    if((i in check)):
        count+=1

print(count)