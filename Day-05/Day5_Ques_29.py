# input hello-----world // hello-----wo----rld
# output ----------helloworld.
str="hello-----wo----rld"
str1=""  #count=0
str2=""  #ans=""
for i in str:
    if(i=='-'):
        str1+=i   #count+=1
    else:
        str2+=i   #ans=ans+i
print(str1+str2)  #print("-"*count+ans)

