
#def f(a,L=[]):
#	L.append(a)
#	return L


def f(a,L=None):
		L=[]
		L.append(a)
		return L


print(f(1))
print(f(2))
print(f(3))
print(f(4))