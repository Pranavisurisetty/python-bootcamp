# 5.find max elem in an array
''' already done'''
# 6.find 2nd max elem in an array

n=int(input("Enter number of elements:"))
a=[]
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest element is:",a[n-2])