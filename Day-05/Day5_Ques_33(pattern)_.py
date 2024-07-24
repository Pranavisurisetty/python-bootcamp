# print lower triangular matrix
for i in range(5):
    for j in range(5):
       if(i!=j and i>j):
          print("*",end="")
       else:
           print("",end="")
    print()