# find the elem present in K+N index.
# k is given by user.ex:i)K=3 & N=2 & ii)K=3;N=4
# input parameters are:i)3 6 8 4 61 2. ii)80 70 54 36 72.
# # op:i)2 ii)error
lst=list(map(int,input().split()))
k=int(input())
n=int(input())
if(len(lst)<(k+n)):
    print("error")
else:
    for i in lst:
        a=(lst[k+n])
    print(a)