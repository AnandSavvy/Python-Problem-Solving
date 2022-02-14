#creating a list
list=["a","b","c","d"]
print("1) created list : ",list)

print(type(list))

# Slice operation on list

print(list[0])

print(list[::])

print(list[::2])

print(list[::-1])

print(list[::-2])

print(list[0:10])

print(list[0:10:2])

print(list[0:-3])

print(list[0:])

print(list[0:0])

# print(list[0::0])  # raise error, because step can not be 0


#appending elements in a list
list.append("e")
print("2) list after append operation : ",list)

#accessing item in a list
print("3) accessing items in a list : ",list[1])

#changing item in a list
list[1]="A"
print("4) changing item in the list : ",list)

#removing item in a list
list.remove("a")
print("5) after removing an item : ",list)

#remove item in a specified index
print("6) after pop operation ; ",list.pop(3))

#loop through a list
print("loop through list:")
for i in list:
    print(i)

#sort function
print(" performing sort on list")
L1=[1,2,3,7,3,9,2,]
L1.sort()
print(L1)

#coping a list
print("coping list")
L2=list.copy()
print(L2)

#joining two list
print(" joining two list")
L3=L1+L2
print(L3)

#appending one list into the other list
print("appending one list into the other list")
for i in L2:
    L1.append(i)
print(L1)

#extend()
print(" extend methon")
list.extend(L2)
print(list)