# How to use a for loop and the enumerate() function in Python
# In this example, we want to print out a list of directions going from Times Square to the Juilliard School of Music in New York City, New York.

#We first have to create the list of directions:

directions = [
    'Head north on Broadway toward W 48th St',
    'Turn left onto W 58th St',
    'Turn right onto 8th Ave',
    'Turn left onto Broadway',
    'Turn left onto Lincoln Center Plaza',
    'Turn right onto Jaffe Dr',
    'Turn left onto Broadway',
    'Turn left onto W 65th St'
]
#Then in the for loop, we create the count and direction loop variables.

#The enumerate() function will take in the directions list and start arguments. We want to start counting at 1 instead of the default of 0.  

for count, direction in enumerate(directions, start=1):
#Inside the loop we will print out the count and direction loop variables.

    print(count, direction)




