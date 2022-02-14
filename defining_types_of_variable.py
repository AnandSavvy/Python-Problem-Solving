# int
n=1929
print(n)
print(type(n))

# float
f=1729.653
print(f)
print(type(f))

# complex
c1=10+2j
print(c1)
print(type(c1))

c2=20-76j
print(c2)
print(type(c2))

c3=c1+c2
print(c3)
print(type(c3))

print("Complex Sum : ",c2)

sum1=n+f
print("Sum of {} and {} is {}".format(n,f,sum1))
print(type(sum1))

sum2=n+f+c1
print("Sum of {} , {} and {} is {}".format(n,f,c1,sum2))
print(type(sum2))