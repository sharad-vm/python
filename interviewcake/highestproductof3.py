def highest_product_of_3(list):
    if len(list)<3:
        raise ValueError("Less than 3 items!")
    
    #Store and update the highest number, highest product of 3 and
    #2 integers, lowest and lowest product of 2 integers
    #lowest because,  2 low -ve numbers can result in a high +ve product
    highest_product_of_3 = list[0] * list[1] * list[2]
    highest_product_of_2 = list[0] * list[1]
    highest = max(list[0], list[1])
    lowest_product_of_2 = list[0] * list[1]
    lowest = min(list[0], list[1])
 
    #Iterate from 3rd element because, we initialized our variables
    #already with the first 2 integers
    for i in range(2, len(list)):
        current = list[i]
        
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)
        
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)
                                   
        highest = max(highest, current)
        
        lowest_product_of_2 = min(lowest_product_of_2,
                                   current * highest,
                                   current * lowest)
                                   
        lowest = min(lowest, current)
        
    return highest_product_of_3

###Test

list=[1,-3,7,4,11,-100]
highest_product_of_3(list)
