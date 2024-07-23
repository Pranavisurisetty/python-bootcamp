# write a prgrm to print prime num in a given range
#order of n*n(brutt force algo)
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)