string=input("enter the string:")
length=len(string)
for row in range (length):
   for col in range(0,row+1):
       print(string[col],end=' ')
print()

