list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# modify item
list1[1][2][2][1] = 3500
# print final result
print(list1)
print(list1[1]) #= [10, 15, [20, 25, [30, 400], 40], 45]
print(list1[1][2]) #= [20, 25, [30, 400], 40]
print(list1[1][2][2])# = [30, 40]
print(list1[1][2][2][1])# = 40