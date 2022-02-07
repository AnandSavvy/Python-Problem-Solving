for num in range(35):  
    # Numbers which are divisible by 15, that means it is divisible by both 3 and 5,   
# it will print "Fizz_Buzz"    # at the place of the number  
    if num % 15 == 0:  
        print(" Fizz_Buzz ")                                          
        continue  
    # Numbers which are dividable by 3, it will print "Fizz"  
    # at the place of the number  
    elif num % 3 == 0:      
        print(" Fizz")                                          
        continue  
    # Numbers which are dividable by 5,  
    # it will print "Buzz" at the  
    # place of the number  
    elif num % 5 == 0:          
        print(" Buzz ")                                      
        continue   
    # in result it will Print numbers  
    print(num)  