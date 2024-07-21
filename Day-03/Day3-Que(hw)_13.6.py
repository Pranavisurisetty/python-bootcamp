# 7.find the sum of squares of given num
def squaresum(n):
    n =int(input())
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i * i)
    return sum
n = 4
print(squaresum(n))
