# take input as hello123world and print output as 6 (1+2+3)
n="hello123world"
d="123456789"
inp=0
for i in n:
    if i in d:
       inp+=int(i)
print(inp)