# remove duplicate elem in the list and print new list.
list=(list(map(int,input().split())))
new_list=[]
for i in list:
    if(i not in new_list):
        new_list.append(i)
print(new_list)