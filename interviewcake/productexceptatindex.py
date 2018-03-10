def product_except_index(list):
    if len(list) <2:
        raise IndexError("Need at least 2 elements in the index to get product.")
    
    #This acts as a placeholder for result set with the length of 
    #the list as long as the input list
    product_except_at_index = [None] * len(list)
    
    #This gets the product of all elements before each index
    #and stores in the placeholder list at it's corresponding index
    product_so_far = 1
    for i in range(len(list)):
        product_except_at_index[i] = product_so_far
        product_so_far *= list[i]
        
    #Instead of creating a new list for products after each index
    #this multiplies the product before each index with the product
    #after each index and appends the list by traversing the input
    #list in the reverse direction
    product_so_far = 1
    for i in range(len(list)-1, -1, -1):
        product_except_at_index[i] *=  product_so_far
        product_so_far *= list[i]
        
    return product_except_at_index


###Test

list = [1,7,3,4]
product_except_index(list)
