str=input("enter a string:")
length=len(str)
for i in range(length):
    for col in range(i+1):
        print(str[col],end="  ")
    print()