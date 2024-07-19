#palindrome or not

n = input("enter the value:")
reverse = n[::-1]
if(n == reverse):
    print("yes it is a palindrome")
else:
   print("no it is not a palindrome")
