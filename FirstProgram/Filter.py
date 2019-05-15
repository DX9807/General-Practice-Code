from functools import*

nums=[2,5,3,6,4,9,7,8,2,4]

evens=list(filter(lambda n:n%2==0,nums))
print(evens)

doubles=list(map(lambda n:n*2,evens))
print(doubles)

reduced=(reduce(lambda a,b:a+b,doubles))
print(reduced)