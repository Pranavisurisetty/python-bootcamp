# Take a space separated i/p from the user and print alternate elements.

my_list=list(map(int,input().split()))
n=len(my_list)
for i in range(0,n,2):
    print(my_list[i])


