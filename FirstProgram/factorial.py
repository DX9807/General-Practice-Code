def fact(n):
   if n==0:
       return 1
   return n*fact(n-1)

x=int(input("Enter the Number:"))
result=fact(x)
print("Factorial of the entered number is:",result)