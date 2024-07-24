# Remove all the brackets from the given algebraic expression
'''str="[(a+b)+c]"
a=""
d="(),[],{}"
for i in str:
    if i not in d:
        a+=i
print(a)'''

# using ascii values for removing brackets.
#}-125;{-123;( )-41,40;[]-91,93
str="{([a+b]+c)}"
sum=0
for i in str:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")
print() 
