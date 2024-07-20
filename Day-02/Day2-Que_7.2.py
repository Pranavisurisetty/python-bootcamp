# how many even numbers are there in above ques
lst=list(map(int,input().split()))
count=0
for i in range(1,len(lst),2):
    count+=1
print(count)