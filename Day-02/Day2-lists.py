#list is mutable--> we can change the values even after declaration of the list

# 1.append--> adding an element at end of the list
# 2.insert--> we can insert any where using index value
# 3.reverse-->2 ways to achieve 1.by using reverse method;2.by using slice method
# 4.sort--> sort in ascending is default;quick sort is used n(logn)-time complexity
# 5.copy--> copy the sm elements.
# 6.pop--> delete the last elem
# 7.count-->counts the elem in the list

#performing operations on list
'''
my_list_1=[1,2,3,4]
my_list.pop(2)
'''
'''
print(my_list)
print(my_list)
print(*my_list,)-->removes (,) & brackets([])
...

#appending
#my_list.append(56)
#print(my_list)

#my_list.insert(4,45)
#print(my_list)
'''
#adding lists
#my_list_1=[1,2,3,4]
# my_list_2=[5,6,7,8]
# new_list=my_list_1+my_list_2
# print(new_list)

# new_list.pop()#removes the last elem
# print(new_list)
'''
my_list_3=[1,2,3,2,4,2,2,5,2,6,]
cnt=my_list_3.count(2)
print(cnt)
'''
# my_list_3=[1,2,3,2,4,2,2,5,2,6,]
# my_list_3.sort()
# print(my_list_3)
'''
my_list_4=[1,2,3,2,4,2,2,5,2,6,]
my_list_4.append(45)
print(my_list_4)
'''
# my_list_4=[1,2,3,2,4,2,2,5,2,6,]
# my_list_4.reverse()
# print(my_list_4)

'''
my_list=list(map(int,input().split))
'''
#map--> more than one input
#input().split- default space separated;
#int--> interger as input
'''
my_list=list(map(int,input().split()))
print(my_list)
'''
# my_list=list(map(int,input().split(",")))
# print(*my_list)
# my_list=list(map(str,input().split()))
# print(*my_list)

# Ques: Take input from the User
# 1.append
# 2.pop
# 3.sort
# 4.hello,length=

my_list=list(map(int,input().split()))
choice=int(input("enter your choice"))
if(choice==1):
    print(my_list.append(6))
elif(choice==2):
    print(my_list.pop())
elif(choice==3):
    print(my_list.sort())
elif(choice==4):
    print(my_list.len())
print(my_list)
    # print("wrong choice")

