






def fib(n):
	 """printing the list of fibbonaci series of nubersupto n"""
     a,b=0,1
     result=[]
     while a<n:
         result.append(a)
         a,b=b,a+b
         return result



n=int(input("Enter the number of terms::"))
f=fib(n)
print(f)
