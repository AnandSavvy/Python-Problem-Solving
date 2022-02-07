s_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", s_list)

count_dict = dict()
for item in s_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)