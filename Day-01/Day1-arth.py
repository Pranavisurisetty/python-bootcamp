#a=int(input())
#b=int(input())
# print(a+b)
# print(a-b)
# print(a/b)
'''
 print(a%b)
 print(a**b)
 print(a*b) 

age=int(input())
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("two and four wheeler")
else:
    print("all") 
    '''
# X went to market 
# 10 apples,2dozen bananas,8 oranges a-15rs,b-4rs,o-5rs.
# ms'y'--x-->700 
'''
f1=int(input())
f2=int(input())
f3=int(input())
a=f1*15
b=f2*4
o=f3*5
sum=(a+b+o)
print(sum)
if(sum<700):
    print( "x not got cheated")
else:
    print(" x got cheated")
'''
'''
# +ve and even=+even.no; -ve and even=-even.no
# +ve and odd=+odd.no; -ve and odd=-odd.no
a=int(input())
if(a%2==0 and a>0):
    print("even positive num")
elif(a%2==0 and a<0):
    print(" even neg num")
elif(a%2!=0 and a<0):
    print("odd neg num")
elif(a%2!=0 and a>0):
    print("odd positive num")
else:
    print("0")
'''
# ms.z is selected for olympics participating in swimming compitition only 1 winner selected among all
# ms.y is participating in table tennies 
# ms.x is participating in badminton
#acc to the selection comm criteria for badminton
# badmintion height=140cm;weight=factors of 2;body fat is =<12%;
#acc to the selection comm criteria for tabletennies are 
#height=118-148cm,weight=fac of no.of medals won by ms.Z,body fat=14%
#acc to previous history z particpated in 14 games.out of which he is having success rate of 50%.
#write a prgrm to check whether x,y,z travel in sm plane from india
 
height=int(input())
weight=int(input())
if(height<=140 and weight%2==0):
    print("selected for badminton")
elif((height>118 and height<148) and weight%5==0):
    print("selected for table tennies")

