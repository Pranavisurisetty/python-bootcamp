# find the missing num in a given sequence of nums
list=list(map(int,input().split()))
n=int(input())
sum=n*(n+1)/2-sum(list)
print(sum)
