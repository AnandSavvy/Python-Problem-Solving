def smart_division(fun_):
	def inner(x,y):
		if y==0:
			print("hi..") 
		else:
			print("hello..")
			return fun_(x,y)
	return inner;
#@smart_division 
def divide(a,b):
	return a/b;
d=smart_division(divide)
print(d (1,2))