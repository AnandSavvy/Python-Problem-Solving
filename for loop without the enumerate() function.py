dogs = ['Harley', 'Phantom', 'Lucky', 'Dingo']
count = 0
for name in dogs:
    count = count  + 1
    print(count, name)


#       OUTPUT 

# 1 Harley
# 2 Phantom
# 3 Lucky
# 4 Dingo

dogs = ['Harley', 'Phantom', 'Lucky', 'Dingo']
count = 0
for name in dogs:
     print(count, name)


#      OUTPUT

# 0 Harley
# 0 Phantom
# 0 Lucky
# 0 Dingo

for name in dogs:
    print(count, name)
    count += 1